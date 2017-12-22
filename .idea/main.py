# coding=utf-8
from tkinter import Button, Tk
from settings import GUI, Params
from chain import Chain
from matplotlib import gridspec
from time import sleep
import random

#---------End of imports
#---------------------------
random.seed(a=None)
root = Tk()

#Init, creating class objects
gs = gridspec.GridSpec(0, 3)
params = Params()
user_interface = GUI(root,params)
chain1 = Chain(user_interface,params.chain1_len,color="gray")
chain2 = Chain(user_interface,params.chain2_len,color="red",second=True)
chain1.draw_chain()
chain2.draw_chain()


#Reset button
def RESET():
    chain1.reset()
    if user_interface.variable_chain_2_checkbutton == 1:
        chain2.reset()
button_reset = Button(root,text="Reset",command=RESET,width=15)
button_reset.grid(column=0,row=4,sticky='nw')

root.mainloop()