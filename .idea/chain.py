# coding=utf-8
from numpy import arange, zeros
from random import uniform, randint
from math import exp, sqrt, pow

class Chain(object):
    """Class contains information about a single DNA chain, its movement and drawing"""

    def __init__(self, user_interface,chain_len,color,second=False):
        #window
        self.user_interface = user_interface
        self.canvas = user_interface.canvas
        self.root = user_interface.root
        self.color = color
        self.second = second
        self.drawing_skip = 30

        self.probability = [0 for x in range(2)]
        self.chain_len = chain_len
        self.dxy = 10 #rozmiar kulki
        #1D position
        self.xLattice = [30 for x in range(self.chain_len)]
        self.yLattice = [917 for x in range(self.chain_len)]
        #atom speed in pixels
        self.move = user_interface.grid/2
        #aditional variables
        self.spacing = 5
        self.line_width = 3
        self.cell_lim = 2*self.spacing+0.1
        self.next_cell_lim = 40
        #2D positions
        self.xLattice = [729.5 for x in range(self.chain_len)]
        self.yLattice = [917 for x in range(self.chain_len)]
        #calculate random initial positions
        self.chain_starting_positions()
        self.dist = (0,0)

        if not self.second:
            self.chain = [self.canvas.create_oval(self.xLattice[i],self.yLattice[i],self.xLattice[i]+self.dxy,self.yLattice[i]+self.dxy,fill=self.color, outline=self.color) for i in range(0,self.chain_len)]
            self.links = [self.canvas.create_line(self.xLattice[i]+self.dxy/2,self.yLattice[i]+self.dxy/2,self.xLattice[i+1]+self.dxy/2,self.yLattice[i+1]+self.dxy/2, fill =self.color,width=self.line_width) for i in range (0,self.chain_len-1)]

    def distance(self,atom_number):
        """function claculates distance between atoms in chain"""
        if atom_number==self.chain_len-1:

            dist_prev = sqrt(pow(self.xLattice[atom_number]-self.xLattice[atom_number-1],2)+pow(self.yLattice[atom_number]-self.yLattice[atom_number-1],2))
            dist_next = 100.
            return {'prev':dist_prev,'next':dist_next}

        elif atom_number==0:

            dist_prev = 100.
            dist_next = sqrt(pow(self.xLattice[atom_number]-self.xLattice[atom_number+1],2)+pow(self.yLattice[atom_number]-self.yLattice[atom_number+1],2))
            return {'prev':dist_prev,'next':dist_next}

        else:

            dist_prev = sqrt(pow(self.xLattice[atom_number]-self.xLattice[atom_number-1],2)+pow(self.yLattice[atom_number]-self.yLattice[atom_number-1],2))
            dist_next = sqrt(pow(self.xLattice[atom_number]-self.xLattice[atom_number+1],2)+pow(self.yLattice[atom_number]-self.yLattice[atom_number+1],2))
            return {'prev':dist_prev,'next':dist_next}

    def chain_starting_positions(self):
        """function randomly defines initial positions of atoms in chain"""
        for i in range (0,self.chain_len):

            rand=randint(1,4)

            if rand==1:
                self.xLattice[i]+=self.spacing
                self.yLattice[i]-=self.spacing
            elif rand==2:
                self.xLattice[i]+=2*self.spacing
            elif rand==3:
                self.xLattice[i]+=self.spacing
                self.yLattice[i]+=self.spacing
            else:
                continue

    def check_same(self, dist, next_prev):

        if dist[next_prev]<=self.cell_lim:
            return True
        else:
            return False

    def check_next_prev(self,dist,atom_number, dir, next_prev='prev'):
        #moving possibilities for first/last atom in chain
        if atom_number==0 or atom_number==self.chain_len-1:
            if atom_number==0:
                var=1
                next_prev='next'
            else:
                var=-1
                next_prev='prev'
            end=var
            #if next/prev atom in the same cell
            dist = self.distance(atom_number)
            if self.check_same(dist,next_prev):
                self.move_at(dir,atom_number)

                return
            #if atom in another cell
            #nw
            if dir=='nw':
                if self.xLattice[atom_number]>self.xLattice[atom_number+var] and self.yLattice[atom_number]>self.yLattice[atom_number+var]:
                    if dist[next_prev]>self.cell_lim and dist[next_prev]<self.next_cell_lim:
                        self.move_at(dir,atom_number)

                        return
            #ne
            elif dir=='ne':
                if self.xLattice[atom_number]<self.xLattice[atom_number+var] and self.yLattice[atom_number]>self.yLattice[atom_number+var]:
                    if dist[next_prev]>self.cell_lim and dist[next_prev]<self.next_cell_lim:
                        self.move_at(dir,atom_number)

                        return
            #sw
            elif dir=='sw':
                if self.xLattice[atom_number]>self.xLattice[atom_number+var] and self.yLattice[atom_number]<self.yLattice[atom_number+var]:
                    if dist[next_prev]>self.cell_lim and dist[next_prev]<self.next_cell_lim:
                        self.move_at(dir,atom_number)

                        return
            #se
            else:
                if self.xLattice[atom_number]<self.xLattice[atom_number+var] and self.yLattice[atom_number]<self.yLattice[atom_number+var]:
                    if dist[next_prev]>self.cell_lim and dist[next_prev]<self.next_cell_lim:
                        self.move_at(dir,atom_number)

                        return

        #moving possibilities for middle atoms
        if atom_number!=0 and atom_number!=self.chain_len-1:

            #nw
            if dir=='nw':
                if self.check_same(dist, 'prev'):
                    if self.xLattice[atom_number]>self.xLattice[atom_number+1] and self.yLattice[atom_number]>self.yLattice[atom_number+1]:
                        if dist['next']>self.cell_lim:
                            self.move_at(dir,atom_number)
                            return
                if self.check_same(dist, 'next'):
                    if self.xLattice[atom_number]>self.xLattice[atom_number-1] and self.yLattice[atom_number]>self.yLattice[atom_number-1]:
                        if dist['prev']>self.cell_lim:
                            self.move_at(dir,atom_number)
                            return

            #ne
            elif dir=='ne':
                if self.check_same(dist, 'prev'):
                    if self.xLattice[atom_number]<self.xLattice[atom_number+1] and self.yLattice[atom_number]>self.yLattice[atom_number+1]:
                        if dist['next']>self.cell_lim:
                            self.move_at(dir,atom_number)
                            return
                if self.check_same(dist, 'next'):
                    if self.xLattice[atom_number]<self.xLattice[atom_number-1] and self.yLattice[atom_number]>self.yLattice[atom_number-1]:
                        if dist['prev']>self.cell_lim:
                            self.move_at(dir,atom_number)
                            return

            #sw
            elif dir=='sw':
                if self.check_same(dist, 'prev'):
                    if self.xLattice[atom_number]>self.xLattice[atom_number+1] and self.yLattice[atom_number]<self.yLattice[atom_number+1]:
                        if dist['next']>self.cell_lim:
                            self.move_at(dir,atom_number)
                            return
                if self.check_same(dist, 'next'):
                    if self.xLattice[atom_number]>self.xLattice[atom_number-1] and self.yLattice[atom_number]<self.yLattice[atom_number-1]:
                        if dist['prev']>self.cell_lim:
                            self.move_at(dir,atom_number)
                            return

            #se
            else:

                if self.check_same(dist, 'prev'):
                    if self.xLattice[atom_number]<self.xLattice[atom_number+1] and self.yLattice[atom_number]<self.yLattice[atom_number+1]:
                        if dist['next']>self.cell_lim:
                            self.move_at(dir,atom_number)
                            return
                if self.check_same(dist, 'next'):
                    if self.xLattice[atom_number]<self.xLattice[atom_number-1] and self.yLattice[atom_number]<self.yLattice[atom_number-1]:
                        if dist['prev']>self.cell_lim:
                            self.move_at(dir,atom_number)
                            return

    def draw_links(self):
        for i in range (0, self.chain_len-1):
            self.canvas.delete(self.links[i])
        for i in range (0, self.chain_len-1):
            self.links[i]= self.canvas.create_line(self.xLattice[i]+self.dxy/2,self.yLattice[i]+self.dxy/2,self.xLattice[i+1]+self.dxy/2,self.yLattice[i+1]+self.dxy/2, fill =self.color,width=self.line_width)

    def calc_probability(self):
        """Function calculates probabilities of each direction movement and stores it in 1D-matrix"""
        self.probability[0] = exp(self.user_interface.slider_field.get()/2)
        self.probability[1] = exp(-self.user_interface.slider_field.get()/2)

    def move_at(self, dir, atom_number):
        """Function moves atom and updates matrix, 1,2,3 and 4 means direction(4 direction as follows: 1-nw, 2-ne, 3-sw, 4-se"""
        if dir == 'nw':
            self.xLattice[atom_number]-=self.move
            self.yLattice[atom_number]-=self.move
            self.canvas.move(self.chain[atom_number],-self.move,-self.move)
        elif dir == 'ne':
            self.xLattice[atom_number]+=self.move
            self.yLattice[atom_number]-=self.move
            self.canvas.move(self.chain[atom_number],self.move,-self.move)
        elif dir == 'sw':
            self.xLattice[atom_number]-=self.move
            self.yLattice[atom_number]+=self.move
            self.canvas.move(self.chain[atom_number],-self.move,self.move)
        else:
            self.xLattice[atom_number]+=self.move
            self.yLattice[atom_number]+=self.move
            self.canvas.move(self.chain[atom_number],self.move,self.move)

    def reset(self):

        self.xLattice = [729.5 for x in range(self.chain_len)]
        self.yLattice = [917 for x in range(self.chain_len)]
        self.chain_starting_positions()

        for i in range (0, self.chain_len):
            self.canvas.delete(self.chain[i])
            self.chain[i] = self.canvas.create_oval(self.xLattice[i],self.yLattice[i],self.xLattice[i]+self.dxy,self.yLattice[i]+self.dxy,fill=self.color, outline=self.color)
        for i in range (0, self.chain_len-1):
            self.canvas.delete(self.links[i])
            self.links[i] = self.canvas.create_line(self.xLattice[i]+self.dxy/2,self.yLattice[i]+self.dxy/2,self.xLattice[i+1]+self.dxy/2,self.yLattice[i+1]+self.dxy/2, fill =self.color,width=self.line_width)

    def check_possible_move(self):
        """Function checks possible move of random chosen atom in chain"""
        atom_number = randint(0,self.chain_len-1)
        pdb = uniform(0.,2*self.probability[0]+2*self.probability[1])
        self.dist = self.distance(atom_number)
        dist=self.dist
        #ruch ostatniego atomu łańcucha
        if atom_number==0:
            #ostatni atom chce się ruszyć do góry w lewo
            if pdb<=self.probability[0]:
                self.check_next_prev(dist,atom_number, 'nw','prev')
            #ostatni atom chce się ruszyć do góry w prawo
            elif pdb>self.probability[0] and pdb<=2*self.probability[0]:
                self.check_next_prev(dist,atom_number, 'ne','next')
            #ostatni atom chce się ruszyć do dołu w lewo
            elif pdb>2*self.probability[0] and pdb<=(2*self.probability[0]+self.probability[1]):
                self.check_next_prev(dist,atom_number, 'sw','next')
            #ostatni atom chce się ruszyć do tyłu w prawo
            else:
                self.check_next_prev(dist,atom_number, 'se','next')
        #ruch pierwszego atomu łańcucha
        elif atom_number==self.chain_len-1:
            #pierwszy atom chce się ruszyć do góry w lewo
            if pdb<=self.probability[0]:
                self.check_next_prev(dist,atom_number, 'nw','prev')
            #pierwszy atom chce się ruszyć do góry w prawo
            elif pdb>self.probability[0] and pdb<=2*self.probability[0]:
                self.check_next_prev(dist,atom_number, 'ne','prev')
            #pierwszy atom chce się ruszyć do dołu w lewo
            elif pdb>2*self.probability[0] and pdb<=(2*self.probability[0]+self.probability[1]):
                self.check_next_prev(dist,atom_number, 'sw','prev')
            #pierwszy atom chce się ruszyć do dołu w prawo
            else:
                self.check_next_prev(dist,atom_number, 'se','prev')
        #ruch środkowych atomów
        else:
            #ruch w lewo góra
            if pdb<=self.probability[0]:
                self.check_next_prev(dist,atom_number,'nw')
            #ruch w prawo góra
            elif pdb>self.probability[0] and pdb<=2*self.probability[0]:
                self.check_next_prev(dist,atom_number,'ne')
            #ruch w lewo dół
            elif pdb>2*self.probability[0] and pdb<=(2*self.probability[0]+self.probability[1]):
                self.check_next_prev(dist,atom_number,'sw')
            #ruch w prawo dół
            else:
                self.check_next_prev(dist,atom_number,'se')

    def draw_chain(self):
        """Drawing function for DNA chain"""
        self.calc_probability()
        #deklaracja chain2(wykonuje się tylko raz)
        if self.second:
            if self.user_interface.variable_chain_2_checkbutton == 1:
                if not self.user_interface.stop_param:
                    self.chain = [self.canvas.create_oval(self.xLattice[i],self.yLattice[i],self.xLattice[i]+self.dxy,self.yLattice[i]+self.dxy,fill=self.color, outline=self.color) for i in range(0,self.chain_len)]
                    self.links = [self.canvas.create_line(self.xLattice[i]+self.dxy/2,self.yLattice[i]+self.dxy/2,self.xLattice[i+1]+self.dxy/2,self.yLattice[i+1]+self.dxy/2, fill =self.color,width=self.line_width) for i in range (0,self.chain_len-1)]

                    self.second = False

        #wyłączenie chain2
        if not self.user_interface.variable_chain_2_checkbutton == 1:
            if self.color == "limegreen":
                if not self.second:
                    for i in range (0, self.chain_len):
                        self.canvas.delete(self.links[i-1])
                        self.canvas.delete(self.chain[i])

        #rysowanie chain2
        if self.user_interface.variable_chain_2_checkbutton == 1 and self.color=="limegreen":
            if not self.user_interface.stop_param:
                for i in range(self.drawing_skip):
                    self.check_possible_move()
                self.draw_links()

        #rysowanie chain1
        elif self.color=="gray":
            if not self.user_interface.stop_param:
                for i in range(self.drawing_skip):
                    self.check_possible_move()
                self.draw_links()

        #ponowienie rysowania co krok wskazany na suwaku "Speed"
        self.canvas.after(105-self.user_interface.speed, self.draw_chain)