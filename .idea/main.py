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
gs = gridspec.GridSpec(0, 2, width_ratios=[3, 1])
sim_settings = Settings(root)
chain1 = Chain(sim_settings.chain1_len)
chain2 = Chain(sim_settings.chain2_len)
probability = fnc.calc_probability(sim_settings)

#inicjalizacja okna i pól wykresów
canvas = Canvas(root,width = 500,height = 600)
canvas.grid(row=0, column=1, columnspan=2, rowspan=10,sticky='ewns')
ball = canvas.create_oval(30,30,100,100,fill="red")

#RESET BUTTON
def RESET():
    chain1.reset()
    chain2.reset()
button_reset = Button(root,text="Reset",command=RESET,width=15)
button_reset.grid(column=0,row=5,sticky='nw')
def draw():
    canvas.move(ball,0.1,0.1)
    canvas.after(1, draw)
draw()
root.mainloop()


