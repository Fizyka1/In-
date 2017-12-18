# coding=utf-8
from tkinter import Button, Tk
import random
from settings import GUI, Params
from chain import Chain
from matplotlib import gridspec
from time import sleep

#---------End of imports
#---------------------------
random.seed(a=None)
root = Tk()

#Init, creating class objects
gs = gridspec.GridSpec(0, 3)
params = Params()
user_interface = GUI(root,params)
chain1 = Chain(user_interface,params)
chain1.draw_chain()
chain1.check_possible_move()

#Reset button
def RESET():
    chain1.reset()
button_reset = Button(root,text="Reset",command=RESET,width=15)
button_reset.grid(column=0,row=5,sticky='nw')

root.mainloop()