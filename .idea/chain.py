# coding=utf-8
from numpy import arange, zeros
from random import uniform, randint

class Chain(object):
    """Klasa zawierająca informacje o pojedyńczym łańcuchu DNA"""

    def __init__(self,chain_len):
        #informacje o atomie
        self.chain_len = chain_len
        self.xLattice = [10.5 for x in range(self.chain_len)]
        self.yLattice = [0.5 for x in range(self.chain_len)]
        self.x = arange(1, self.chain_len+1, 1)
        self.move = 1

    def check_possible_move(self,probability):
        """Funkcja losująca atom łańcucha, sprawdzająca możliwość ruchu i zmieniająca jego położenie"""
        atom_number=randint(0,self.chain_len-1)
        pdb=uniform(0.,2*probability[0]+2*probability[1])
        #sprawdzanie możliwości ruchu wyjątków kiedy atomy na końcu i początku łańcucha mają tylko jednego sąsiada

        if atom_number==0:
            if pdb<=probability[0]:
                #pierwszy atom chce się ruszyć do góry w lewo
                if self.yLattice[atom_number]==self.yLattice[atom_number+1] and self.xLattice[atom_number]==self.xLattice[atom_number+1]:
                    self.xLattice[atom_number]-=1
                    self.yLattice[atom_number]+=1
                elif self.yLattice[atom_number]+1==self.yLattice[atom_number+1] and self.xLattice[atom_number]-1==self.xLattice[atom_number+1]:
                    self.xLattice[atom_number]-=1
                    self.yLattice[atom_number]+=1
            elif pdb>probability[0] and pdb<=2*probability[0]:
                #pierwszy atom chce się ruszyć do gó©y w prawo
                if self.yLattice[atom_number]==self.yLattice[atom_number+1] and self.xLattice[atom_number]==self.xLattice[atom_number+1]:
                    self.xLattice[atom_number]+=1
                    self.yLattice[atom_number]+=1
                elif self.yLattice[atom_number]+1==self.yLattice[atom_number+1] and self.xLattice[atom_number]+1==self.xLattice[atom_number+1]:
                    self.xLattice[atom_number]+=1
                    self.yLattice[atom_number]+=1
            elif pdb>2*probability[0] and pdb<=(2*probability[0]+probability[1]):
                #pierwszy atom chce się ruszyć do dołu w lewo
                if self.yLattice[atom_number]==self.yLattice[atom_number+1] and self.xLattice[atom_number]==self.xLattice[atom_number+1]:
                    self.xLattice[atom_number]-=1
                    self.yLattice[atom_number]-=1
                elif self.yLattice[atom_number]-1==self.yLattice[atom_number+1] and self.xLattice[atom_number]-1==self.xLattice[atom_number+1]:
                    self.xLattice[atom_number]-=1
                    self.yLattice[atom_number]-=1
            else:
                #pierwszy atom chce się ruszyć do tyłu w prawo
                if self.yLattice[atom_number]==self.yLattice[atom_number+1] and self.xLattice[atom_number]==self.xLattice[atom_number+1]:
                    self.xLattice[atom_number] += 1
                    self.yLattice[atom_number] -= 1
                elif self.yLattice[atom_number]-1 == self.yLattice[atom_number+1] and self.xLattice[atom_number]+1 == self.xLattice[atom_number+1]:
                    self.xLattice[atom_number] += 1
                    self.yLattice[atom_number] -= 1

        elif atom_number==self.chain_len-1:
            #Kiedy pierwszy atom łańcucha może poruszyć się w każdą stronę
            if pdb<=probability[0]:
                #pierwszy atom chce się ruszyć do góry w lewo
                if self.yLattice[atom_number]==self.yLattice[atom_number-1] and self.xLattice[atom_number]==self.xLattice[atom_number-1]:
                    self.xLattice[atom_number]-=1
                    self.yLattice[atom_number]+=1
                elif self.yLattice[atom_number]+1==self.yLattice[atom_number-1] and self.xLattice[atom_number]-1==self.xLattice[atom_number-1]:
                    self.xLattice[atom_number]-=1
                    self.yLattice[atom_number]+=1
            elif pdb>probability[0] and pdb<=2*probability[0]:
                #pierwszy atom chce się ruszyć do gó©y w prawo
                if self.yLattice[atom_number]==self.yLattice[atom_number-1] and self.xLattice[atom_number]==self.xLattice[atom_number-1]:
                    self.xLattice[atom_number]+=1
                    self.yLattice[atom_number]+=1
                elif self.yLattice[atom_number]+1==self.yLattice[atom_number-1] and self.xLattice[atom_number]+1==self.xLattice[atom_number-1]:
                    self.xLattice[atom_number]+=1
                    self.yLattice[atom_number]+=1
            elif pdb>2*probability[0] and pdb<=(2*probability[0]+probability[1]):
                #pierwszy atom chce się ruszyć do dołu w lewo
                if self.yLattice[atom_number]==self.yLattice[atom_number-1] and self.xLattice[atom_number]==self.xLattice[atom_number-1]:
                    self.xLattice[atom_number]-=1
                    self.yLattice[atom_number]-=1
                elif self.yLattice[atom_number]-1==self.yLattice[atom_number-1] and self.xLattice[atom_number]-1==self.xLattice[atom_number-1]:
                    self.xLattice[atom_number]-=1
                    self.yLattice[atom_number]-=1
            else:
                #pierwszy atom chce się ruszyć do tyłu w prawo
                if self.yLattice[atom_number]==self.yLattice[atom_number-1] and self.xLattice[atom_number]==self.xLattice[atom_number-1]:
                    self.xLattice[atom_number]+=1
                    self.yLattice[atom_number]-=1
                elif self.yLattice[atom_number]-1==self.yLattice[atom_number-1] and self.xLattice[atom_number]+1==self.xLattice[atom_number-1]:
                    self.xLattice[atom_number]+=1
                    self.yLattice[atom_number]-=1
        #sprawdzanie możliwości ruchu pozostałych atomów w łańcuchu
        else:
            if pdb<=probability[0]:
                if self.yLattice[atom_number]+1==self.yLattice[atom_number+1] and self.xLattice[atom_number]-1==self.xLattice[atom_number+1]:
                    if self.yLattice[atom_number]==self.yLattice[atom_number-1] and self.xLattice[atom_number]==self.xLattice[atom_number-1]:
                        self.yLattice[atom_number]+=1
                        self.xLattice[atom_number]-=1
                if self.yLattice[atom_number]+1==self.yLattice[atom_number-1] and self.xLattice[atom_number]-1==self.xLattice[atom_number-1]:
                    if self.yLattice[atom_number]==self.yLattice[atom_number+1] and self.xLattice[atom_number]==self.xLattice[atom_number+1]:
                        self.yLattice[atom_number]+=1
                        self.xLattice[atom_number]-=1
            elif pdb>probability[0] and pdb<=2*probability[0]:
                if self.yLattice[atom_number]+1==self.yLattice[atom_number+1] and self.xLattice[atom_number]+1==self.xLattice[atom_number+1]:
                    if self.yLattice[atom_number]==self.yLattice[atom_number-1] and self.xLattice[atom_number]==self.xLattice[atom_number-1]:
                        self.yLattice[atom_number]+=1
                        self.xLattice[atom_number]+=1
                if self.yLattice[atom_number]+1==self.yLattice[atom_number-1] and self.xLattice[atom_number]+1==self.xLattice[atom_number-1]:
                    if self.yLattice[atom_number]==self.yLattice[atom_number+1] and self.xLattice[atom_number]==self.xLattice[atom_number+1]:
                        self.yLattice[atom_number]+=1
                        self.xLattice[atom_number]+=1
            elif pdb>2*probability[0] and pdb<=(2*probability[0]+probability[1]):
                if self.yLattice[atom_number]-1==self.yLattice[atom_number+1] and self.xLattice[atom_number]-1==self.xLattice[atom_number+1]:
                    if self.yLattice[atom_number]==self.yLattice[atom_number-1] and self.xLattice[atom_number]==self.xLattice[atom_number-1]:
                        self.yLattice[atom_number]-=1
                        self.xLattice[atom_number]-=1
                if self.yLattice[atom_number]-1==self.yLattice[atom_number-1] and self.xLattice[atom_number]-1==self.xLattice[atom_number-1]:
                    if self.yLattice[atom_number]==self.yLattice[atom_number+1] and self.xLattice[atom_number]==self.xLattice[atom_number+1]:
                        self.yLattice[atom_number]-=1
                        self.xLattice[atom_number]-=1
            else:
                if self.yLattice[atom_number]-1==self.yLattice[atom_number+1] and self.xLattice[atom_number]+1==self.xLattice[atom_number+1]:
                    if self.yLattice[atom_number]==self.yLattice[atom_number-1] and self.xLattice[atom_number]==self.xLattice[atom_number-1]:
                        self.yLattice[atom_number]-=1
                        self.xLattice[atom_number]+=1
                if self.yLattice[atom_number]-1==self.yLattice[atom_number-1] and self.xLattice[atom_number]+1==self.xLattice[atom_number-1]:
                    if self.yLattice[atom_number]==self.yLattice[atom_number+1] and self.xLattice[atom_number]==self.xLattice[atom_number+1]:
                        self.yLattice[atom_number]-=1
                        self.xLattice[atom_number]+=1
    def reset(self):
        self.xLattice = [10.5 for x in range(self.chain_len)]
        self.yLattice = [0.5 for x in range(self.chain_len)]