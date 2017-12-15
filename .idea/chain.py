# coding=utf-8
from numpy import arange, zeros
from random import uniform, randint
from math import exp

class Chain(object):
    """Class contains information about a single DNA chain, its movement and drawing"""

    def __init__(self, sim_settings):
        #informacje o atomie
        self.sim_settings = sim_settings
        self.chain_len = sim_settings.chain1_len
        self.xLattice = [570 for x in range(self.chain_len)]
        self.yLattice = [570 for x in range(self.chain_len)]
        self.x = arange(1, self.chain_len+1, 1)
        self.move = 15
        self.canvas = sim_settings.canvas
        self.probability = [0 for x in range(2)]
        for i in range (self.sim_settings.chain1_len):
            ball = sim_settings.canvas.create_oval(self.xLattice[i],self.yLattice[i],self.xLattice[i]+10,self.yLattice[i]+10,fill="grey", outline='grey')
    def calc_probability(self):
        self.probability[0] = exp(self.sim_settings.slider_field.get()/2)
        self.probability[1] = exp(-self.sim_settings.slider_field.get()/2)
        self.canvas.after(400, self.draw_chain)

        return probability


    def draw_chain(self):
        """Drawing fucntion for DNA chain"""
        for i in range (self.sim_settings.chain1_len):
            ball = self.sim_settings.canvas.create_oval(self.xLattice[i],self.yLattice[i],self.xLattice[i]+10,self.yLattice[i]+10,fill="grey", outline='grey')
        self.canvas.after(self.sim_settings.slider_speed.get(), self.draw_chain)

    def check_possible_move(self):
        """Function checks possible move of random chosen atom in chain"""
        atom_number=randint(0,self.chain_len-1)
        pdb=uniform(0.,2*self.probability[0]+2*self.probability[1])
        #sprawdzanie możliwości ruchu wyjątków kiedy atomy na końcu i początku łańcucha mają tylko jednego sąsiada

        if atom_number==0:
            if pdb<=self.probability[0]:
                #pierwszy atom chce się ruszyć do góry w lewo
                if self.yLattice[atom_number]==self.yLattice[atom_number+1] and self.xLattice[atom_number]==self.xLattice[atom_number+1]:
                    self.xLattice[atom_number]-=self.move
                    self.yLattice[atom_number]+=self.move
                elif self.yLattice[atom_number]+self.move==self.yLattice[atom_number+1] and self.xLattice[atom_number]-self.move==self.xLattice[atom_number+1]:
                    self.xLattice[atom_number]-=self.move
                    self.yLattice[atom_number]+=self.move
            elif pdb>self.probability[0] and pdb<=2*self.probability[0]:
                #pierwszy atom chce się ruszyć do góry w prawo
                if self.yLattice[atom_number]==self.yLattice[atom_number+1] and self.xLattice[atom_number]==self.xLattice[atom_number+1]:
                    self.xLattice[atom_number]+=self.move
                    self.yLattice[atom_number]+=self.move
                elif self.yLattice[atom_number]+self.move==self.yLattice[atom_number+1] and self.xLattice[atom_number]+self.move==self.xLattice[atom_number+1]:
                    self.xLattice[atom_number]+=self.move
                    self.yLattice[atom_number]+=self.move
            elif pdb>2*self.probability[0] and pdb<=(2*self.probability[0]+self.probability[1]):
                #pierwszy atom chce się ruszyć do dołu w lewo
                if self.yLattice[atom_number]==self.yLattice[atom_number+1] and self.xLattice[atom_number]==self.xLattice[atom_number+1]:
                    self.xLattice[atom_number]-=self.move
                    self.yLattice[atom_number]-=self.move
                elif self.yLattice[atom_number]-self.move==self.yLattice[atom_number+1] and self.xLattice[atom_number]-self.move==self.xLattice[atom_number+1]:
                    self.xLattice[atom_number]-=self.move
                    self.yLattice[atom_number]-=self.move
            else:
                #pierwszy atom chce się ruszyć do tyłu w prawo
                if self.yLattice[atom_number]==self.yLattice[atom_number+1] and self.xLattice[atom_number]==self.xLattice[atom_number+1]:
                    self.xLattice[atom_number] += self.move
                    self.yLattice[atom_number] -= self.move
                elif self.yLattice[atom_number]-self.move == self.yLattice[atom_number+1] and self.xLattice[atom_number]+self.move == self.xLattice[atom_number+1]:
                    self.xLattice[atom_number] += self.move
                    self.yLattice[atom_number] -= self.move

        elif atom_number==self.chain_len-1:
            #Kiedy pierwszy atom łańcucha może poruszyć się w każdą stronę
            if pdb<=self.probability[0]:
                #pierwszy atom chce się ruszyć do góry w lewo
                if self.yLattice[atom_number]==self.yLattice[atom_number-1] and self.xLattice[atom_number]==self.xLattice[atom_number-1]:
                    self.xLattice[atom_number]-=self.move
                    self.yLattice[atom_number]+=self.move
                elif self.yLattice[atom_number]+self.move==self.yLattice[atom_number-1] and self.xLattice[atom_number]-self.move==self.xLattice[atom_number-1]:
                    self.xLattice[atom_number]-=self.move
                    self.yLattice[atom_number]+=self.move
            elif pdb>self.probability[0] and pdb<=2*self.probability[0]:
                #pierwszy atom chce się ruszyć do gó©y w prawo
                if self.yLattice[atom_number]==self.yLattice[atom_number-1] and self.xLattice[atom_number]==self.xLattice[atom_number-1]:
                    self.xLattice[atom_number]+=self.move
                    self.yLattice[atom_number]+=self.move
                elif self.yLattice[atom_number]+self.move==self.yLattice[atom_number-1] and self.xLattice[atom_number]+self.move==self.xLattice[atom_number-1]:
                    self.xLattice[atom_number]+=self.move
                    self.yLattice[atom_number]+=self.move
            elif pdb>2*self.probability[0] and pdb<=(2*self.probability[0]+self.probability[1]):
                #pierwszy atom chce się ruszyć do dołu w lewo
                if self.yLattice[atom_number]==self.yLattice[atom_number-1] and self.xLattice[atom_number]==self.xLattice[atom_number-1]:
                    self.xLattice[atom_number]-=self.move
                    self.yLattice[atom_number]-=self.move
                elif self.yLattice[atom_number]-self.move==self.yLattice[atom_number-1] and self.xLattice[atom_number]-self.move==self.xLattice[atom_number-1]:
                    self.xLattice[atom_number]-=self.move
                    self.yLattice[atom_number]-=self.move
            else:
                #pierwszy atom chce się ruszyć do tyłu w prawo
                if self.yLattice[atom_number]==self.yLattice[atom_number-1] and self.xLattice[atom_number]==self.xLattice[atom_number-1]:
                    self.xLattice[atom_number]+=self.move
                    self.yLattice[atom_number]-=self.move
                elif self.yLattice[atom_number]-self.move==self.yLattice[atom_number-1] and self.xLattice[atom_number]+self.move==self.xLattice[atom_number-1]:
                    self.xLattice[atom_number]+=self.move
                    self.yLattice[atom_number]-=self.move
        #sprawdzanie możliwości ruchu pozostałych atomów w łańcuchu
        else:
            if pdb<=self.probability[0]:
                if self.yLattice[atom_number]+self.move==self.yLattice[atom_number+1] and self.xLattice[atom_number]-self.move==self.xLattice[atom_number+1]:
                    if self.yLattice[atom_number]==self.yLattice[atom_number-1] and self.xLattice[atom_number]==self.xLattice[atom_number-1]:
                        self.yLattice[atom_number]+=self.move
                        self.xLattice[atom_number]-=self.move
                if self.yLattice[atom_number]+self.move==self.yLattice[atom_number-1] and self.xLattice[atom_number]-self.move==self.xLattice[atom_number-1]:
                    if self.yLattice[atom_number]==self.yLattice[atom_number+1] and self.xLattice[atom_number]==self.xLattice[atom_number+1]:
                        self.yLattice[atom_number]+=self.move
                        self.xLattice[atom_number]-=self.move
            elif pdb>self.probability[0] and pdb<=2*self.probability[0]:
                if self.yLattice[atom_number]+self.move==self.yLattice[atom_number+1] and self.xLattice[atom_number]+self.move==self.xLattice[atom_number+1]:
                    if self.yLattice[atom_number]==self.yLattice[atom_number-1] and self.xLattice[atom_number]==self.xLattice[atom_number-1]:
                        self.yLattice[atom_number]+=self.move
                        self.xLattice[atom_number]+=self.move
                if self.yLattice[atom_number]+self.move==self.yLattice[atom_number-1] and self.xLattice[atom_number]+self.move==self.xLattice[atom_number-1]:
                    if self.yLattice[atom_number]==self.yLattice[atom_number+1] and self.xLattice[atom_number]==self.xLattice[atom_number+1]:
                        self.yLattice[atom_number]+=self.move
                        self.xLattice[atom_number]+=self.move
            elif pdb>2*self.probability[0] and pdb<=(2*self.probability[0]+self.probability[1]):
                if self.yLattice[atom_number]-self.move==self.yLattice[atom_number+1] and self.xLattice[atom_number]-self.move==self.xLattice[atom_number+1]:
                    if self.yLattice[atom_number]==self.yLattice[atom_number-1] and self.xLattice[atom_number]==self.xLattice[atom_number-1]:
                        self.yLattice[atom_number]-=self.move
                        self.xLattice[atom_number]-=self.move
                if self.yLattice[atom_number]-self.move==self.yLattice[atom_number-1] and self.xLattice[atom_number]-self.move==self.xLattice[atom_number-1]:
                    if self.yLattice[atom_number]==self.yLattice[atom_number+1] and self.xLattice[atom_number]==self.xLattice[atom_number+1]:
                        self.yLattice[atom_number]-=self.move
                        self.xLattice[atom_number]-=self.move
            else:
                if self.yLattice[atom_number]-self.move==self.yLattice[atom_number+1] and self.xLattice[atom_number]+self.move==self.xLattice[atom_number+1]:
                    if self.yLattice[atom_number]==self.yLattice[atom_number-1] and self.xLattice[atom_number]==self.xLattice[atom_number-1]:
                        self.yLattice[atom_number]-=self.move
                        self.xLattice[atom_number]+=self.move
                if self.yLattice[atom_number]-self.move==self.yLattice[atom_number-1] and self.xLattice[atom_number]+self.move==self.xLattice[atom_number-1]:
                    if self.yLattice[atom_number]==self.yLattice[atom_number+1] and self.xLattice[atom_number]==self.xLattice[atom_number+1]:
                        self.yLattice[atom_number]-=self.move
                        self.xLattice[atom_number]+=self.move

    def reset(self):
        self.xLattice = [570 for x in range(self.chain_len)]
        self.yLattice = [570 for x in range(self.chain_len)]