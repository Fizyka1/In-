# coding=utf-8
from numpy import arange, zeros
from random import uniform, randint
from math import exp

class Chain(object):
    """Class contains information about a single DNA chain, its movement and drawing"""

    def __init__(self, user_interface,chain_len,color,second=False):
        #window
        self.user_interface = user_interface
        self.canvas = user_interface.canvas
        self.root = user_interface.root
        self.color = color
        self.second = second
        self.drawing_skip = 50
        self.first_init = True

        self.probability = [0 for x in range(2)]
        self.chain_len = chain_len
        #2D positions
        self.xLattice = [765.5 for x in range(self.chain_len)]
        self.yLattice = [621.5 for x in range(self.chain_len)]
        self.dxy = 7 #rozmiar kulki
        #1D position
        self.x = arange(1, self.chain_len+1, 1)
        #atom speed in pixels
        self.move = 15
        self.line_width = 2

        if not self.second:
            self.chain = [self.canvas.create_oval(self.xLattice[i],self.yLattice[i],self.xLattice[i]+self.dxy,self.yLattice[i]+self.dxy,fill=self.color, outline=self.color) for i in range(0,self.chain_len)]
            self.links = [self.canvas.create_line(self.xLattice[i]+self.dxy/2,self.yLattice[i]+self.dxy/2,self.xLattice[i+1]+self.dxy/2,self.yLattice[i+1]+self.dxy/2, fill =self.color,width=self.line_width) for i in range (0,self.chain_len-1)]
            #self.labels = [self.canvas.create_text((self.xLattice[i]-5, self.yLattice[i]+3), text=str(i)) for i in range (0, self.chain_len)]
            #for i in range (0, self.chain_len):
             #   if i%2==0:
             #       self.canvas.move(self.labels[i],17,0)

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
            #self.canvas.move(self.labels[atom_number],-self.move,-self.move)
        elif dir == 'ne':
            self.xLattice[atom_number]+=self.move
            self.yLattice[atom_number]-=self.move
            self.canvas.move(self.chain[atom_number],self.move,-self.move)
           #self.canvas.move(self.labels[atom_number],self.move,-self.move)
        elif dir == 'sw':
            self.xLattice[atom_number]-=self.move
            self.yLattice[atom_number]+=self.move
            self.canvas.move(self.chain[atom_number],-self.move,self.move)
           #self.canvas.move(self.labels[atom_number],-self.move,self.move)
        else:
            self.xLattice[atom_number]+=self.move
            self.yLattice[atom_number]+=self.move
            self.canvas.move(self.chain[atom_number],self.move,self.move)
           #self.canvas.move(self.labels[atom_number],self.move,self.move)

    def check_possible_move(self):
        """Function checks possible move of random chosen atom in chain"""
        atom_number=randint(0,self.chain_len-1)
        pdb=uniform(0.,2*self.probability[0]+2*self.probability[1])

        #ruch ostatniego atomu łańcucha
        if atom_number==0:
            #ostatni atom chce się ruszyć do góry w lewo
            if pdb<=self.probability[0]:
                if self.yLattice[atom_number]==self.yLattice[atom_number+1] and self.xLattice[atom_number]==self.xLattice[atom_number+1]:
                    self.move_at('nw',atom_number)
                elif self.yLattice[atom_number]-self.move==self.yLattice[atom_number+1] and self.xLattice[atom_number]-self.move==self.xLattice[atom_number+1]:
                    self.move_at('nw',atom_number)
            #ostatni atom chce się ruszyć do góry w prawo
            elif pdb>self.probability[0] and pdb<=2*self.probability[0]:
                if self.yLattice[atom_number]==self.yLattice[atom_number+1] and self.xLattice[atom_number]==self.xLattice[atom_number+1]:
                    self.move_at('ne',atom_number)
                elif self.yLattice[atom_number]-self.move==self.yLattice[atom_number+1] and self.xLattice[atom_number]+self.move==self.xLattice[atom_number+1]:
                    self.move_at('ne',atom_number)
            #ostatni atom chce się ruszyć do dołu w lewo
            elif pdb>2*self.probability[0] and pdb<=(2*self.probability[0]+self.probability[1]):
                if self.yLattice[atom_number]==self.yLattice[atom_number+1] and self.xLattice[atom_number]==self.xLattice[atom_number+1]:
                    self.move_at('sw',atom_number)
                elif self.yLattice[atom_number]+self.move==self.yLattice[atom_number+1] and self.xLattice[atom_number]-self.move==self.xLattice[atom_number+1]:
                    self.move_at('sw',atom_number)
            #ostatni atom chce się ruszyć do tyłu w prawo
            else:
                if self.yLattice[atom_number]==self.yLattice[atom_number+1] and self.xLattice[atom_number]==self.xLattice[atom_number+1]:
                    self.move_at('se',atom_number)
                elif self.yLattice[atom_number]+self.move == self.yLattice[atom_number+1] and self.xLattice[atom_number]+self.move == self.xLattice[atom_number+1]:
                    self.move_at('se',atom_number)
        #ruch pierwszego atomu łańcucha
        elif atom_number==self.chain_len-1:
            #pierwszy atom chce się ruszyć do góry w lewo
            if pdb<=self.probability[0]:
                if self.yLattice[atom_number]==self.yLattice[atom_number-1] and self.xLattice[atom_number]==self.xLattice[atom_number-1]:
                    self.move_at('nw',atom_number)
                elif self.yLattice[atom_number]-self.move==self.yLattice[atom_number-1] and self.xLattice[atom_number]-self.move==self.xLattice[atom_number-1]:
                    self.move_at('nw',atom_number)
            #pierwszy atom chce się ruszyć do góry w prawo
            elif pdb>self.probability[0] and pdb<=2*self.probability[0]:
                if self.yLattice[atom_number]==self.yLattice[atom_number-1] and self.xLattice[atom_number]==self.xLattice[atom_number-1]:
                    self.move_at('ne',atom_number)
                elif self.yLattice[atom_number]-self.move==self.yLattice[atom_number-1] and self.xLattice[atom_number]+self.move==self.xLattice[atom_number-1]:
                    self.move_at('ne',atom_number)
            #pierwszy atom chce się ruszyć do dołu w lewo
            elif pdb>2*self.probability[0] and pdb<=(2*self.probability[0]+self.probability[1]):
                if self.yLattice[atom_number]==self.yLattice[atom_number-1] and self.xLattice[atom_number]==self.xLattice[atom_number-1]:
                    self.move_at('sw',atom_number)
                elif self.yLattice[atom_number]+self.move==self.yLattice[atom_number-1] and self.xLattice[atom_number]-self.move==self.xLattice[atom_number-1]:
                    self.move_at('sw',atom_number)
            #pierwszy atom chce się ruszyć do tyłu w prawo
            else:
                if self.yLattice[atom_number]==self.yLattice[atom_number-1] and self.xLattice[atom_number]==self.xLattice[atom_number-1]:
                    self.move_at('se',atom_number)
                elif self.yLattice[atom_number]+self.move==self.yLattice[atom_number-1] and self.xLattice[atom_number]+self.move==self.xLattice[atom_number-1]:
                    self.move_at('se',atom_number)
        #ruch środkowych atomów
        else:
            #ruch w lewo góra
            if pdb<=self.probability[0]:
                if self.yLattice[atom_number]-self.move==self.yLattice[atom_number+1] and self.xLattice[atom_number]-self.move==self.xLattice[atom_number+1]:
                    if self.yLattice[atom_number]==self.yLattice[atom_number-1] and self.xLattice[atom_number]==self.xLattice[atom_number-1]:
                        self.move_at('nw',atom_number)
                if self.yLattice[atom_number]-self.move==self.yLattice[atom_number-1] and self.xLattice[atom_number]-self.move==self.xLattice[atom_number-1]:
                    if self.yLattice[atom_number]==self.yLattice[atom_number+1] and self.xLattice[atom_number]==self.xLattice[atom_number+1]:
                        self.move_at('nw',atom_number)
            #ruch w prawo góra
            elif pdb>self.probability[0] and pdb<=2*self.probability[0]:
                if self.yLattice[atom_number]-self.move==self.yLattice[atom_number+1] and self.xLattice[atom_number]+self.move==self.xLattice[atom_number+1]:
                    if self.yLattice[atom_number]==self.yLattice[atom_number-1] and self.xLattice[atom_number]==self.xLattice[atom_number-1]:
                        self.move_at('ne',atom_number)
                if self.yLattice[atom_number]-self.move==self.yLattice[atom_number-1] and self.xLattice[atom_number]+self.move==self.xLattice[atom_number-1]:
                    if self.yLattice[atom_number]==self.yLattice[atom_number+1] and self.xLattice[atom_number]==self.xLattice[atom_number+1]:
                        self.move_at('ne',atom_number)
            #ruch w lewo dół
            elif pdb>2*self.probability[0] and pdb<=(2*self.probability[0]+self.probability[1]):
                if self.yLattice[atom_number]+self.move==self.yLattice[atom_number+1] and self.xLattice[atom_number]-self.move==self.xLattice[atom_number+1]:
                    if self.yLattice[atom_number]==self.yLattice[atom_number-1] and self.xLattice[atom_number]==self.xLattice[atom_number-1]:
                        self.move_at('sw',atom_number)
                if self.yLattice[atom_number]+self.move==self.yLattice[atom_number-1] and self.xLattice[atom_number]-self.move==self.xLattice[atom_number-1]:
                    if self.yLattice[atom_number]==self.yLattice[atom_number+1] and self.xLattice[atom_number]==self.xLattice[atom_number+1]:
                        self.move_at('sw',atom_number)
            #ruch w prawo dół
            else:
                if self.yLattice[atom_number]+self.move==self.yLattice[atom_number+1] and self.xLattice[atom_number]+self.move==self.xLattice[atom_number+1]:
                    if self.yLattice[atom_number]==self.yLattice[atom_number-1] and self.xLattice[atom_number]==self.xLattice[atom_number-1]:
                        self.move_at('se',atom_number)
                if self.yLattice[atom_number]+self.move==self.yLattice[atom_number-1] and self.xLattice[atom_number]+self.move==self.xLattice[atom_number-1]:
                    if self.yLattice[atom_number]==self.yLattice[atom_number+1] and self.xLattice[atom_number]==self.xLattice[atom_number+1]:
                        self.move_at('se',atom_number)

    def reset(self):

        self.xLattice = [765.5 for x in range(self.chain_len)]
        self.yLattice = [621.5 for x in range(self.chain_len)]

        for i in range (0, self.chain_len):
            self.canvas.delete(self.chain[i])
            self.chain[i] = self.canvas.create_oval(self.xLattice[i],self.yLattice[i],self.xLattice[i]+self.dxy,self.yLattice[i]+self.dxy,fill=self.color, outline=self.color)
        for i in range (0, self.chain_len-1):
            self.canvas.delete(self.links[i])
            self.links[i] = self.canvas.create_line(self.xLattice[i]+self.dxy/2,self.yLattice[i]+self.dxy/2,self.xLattice[i+1]+self.dxy/2,self.yLattice[i+1]+self.dxy/2, fill =self.color,width=self.line_width)

    def draw_chain(self):
        """Drawing function for DNA chain"""
        self.calc_probability()
        #deklaracja chain2(wykonuje się tylko raz
        if self.second:
            if self.user_interface.variable_chain_2_checkbutton == 1:
                if not self.user_interface.stop_param:
                    self.chain = [self.canvas.create_oval(self.xLattice[i],self.yLattice[i],self.xLattice[i]+self.dxy,self.yLattice[i]+self.dxy,fill=self.color, outline=self.color) for i in range(0,self.chain_len)]
                    self.links = [self.canvas.create_line(self.xLattice[i]+self.dxy/2,self.yLattice[i]+self.dxy/2,self.xLattice[i+1]+self.dxy/2,self.yLattice[i+1]+self.dxy/2, fill =self.color,width=self.line_width) for i in range (0,self.chain_len-1)]
                    #self.labels = [self.canvas.create_text((self.xLattice[i]-5, self.yLattice[i]+3), text=str(i)) for i in range (0, self.chain_len)]
                    #for i in range (0, self.chain_len):
                    #   if i%2==0:
                    #       self.canvas.move(self.labels[i],17,0)
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