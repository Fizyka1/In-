# coding=utf-8
from tkinter import *
import random
import functions as fnc
from settings import Settings
from chain import Chain
from matplotlib import gridspec
from time import sleep

#---------End of imports
#---------------------------
random.seed(a=None)
root = Tk()

#Init, creating class objects
gs = gridspec.GridSpec(0, 3)
sim_settings = Settings(root)
chain1 = Chain(sim_settings)

#RESET BUTTON
def RESET():
    chain1.reset()
button_reset = Button(root,text="Reset",command=RESET,width=15)
button_reset.grid(column=0,row=5,sticky='nw')

chain1.draw_chain()
chain1.check_possible_move()
root.mainloop()


