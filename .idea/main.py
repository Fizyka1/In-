# coding=utf-8
from tkinter import Button, Tk
from settings import GUI, Params
from chain import Chain
from matplotlib import gridspec
import random

#---------End of imports
#---------------------------
random.seed(a=None)
root = Tk()

#Init, creating class objects
params = Params()
user_interface = GUI(root,params)

#creating chains
chain1 = Chain(user_interface,params.chain1_len,color="gray")
chain2 = Chain(user_interface,params.chain2_len,color="limegreen",second=True)

#drawing chains
chain1.draw_chain()
chain2.draw_chain()

#Reset button
def RESET():

    chain1.reset()

    if user_interface.variable_chain_2_checkbutton == 1:
        chain2.reset()

button_reset = Button(user_interface.frame_left_up_lower,image=user_interface.reset_png,command=RESET,width=user_interface.button_size,height=user_interface.button_size)
button_reset.pack(side='top')

#starting window mainloop
root.mainloop()