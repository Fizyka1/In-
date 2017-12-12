# coding=utf-8
import tkinter as Tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import functions as fnc
from settings import Settings
from chain import Chain
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import gridspec
#---------End of imports
#---------------------------
random.seed(a=None)
root = Tk.Tk()
root.wm_attributes('-fullscreen', True)

#Init, creating class objects
fig = plt.Figure(figsize=(16,9))
gs = gridspec.GridSpec(0, 2, width_ratios=[3, 1])
sim_settings = Settings(fig,root)
chain1 = Chain(sim_settings.chain1_len)
chain2 = Chain(sim_settings.chain2_len)
probability = fnc.calc_probability(sim_settings)

#main animating function; here random atoms from chain is chosen and then algorithm checks it's possible moves
def animate(i):

    #stop_param umozliwia kontrole uzytkownika nad postepem symulacji, przerywaniem i wznawianiemm
    if sim_settings.stop_param == 0:
        probability = fnc.calc_probability(sim_settings)
        for x in range(sim_settings.speed):
            chain1.check_possible_move(probability)

        if sim_settings.variable_chain_2_checkbutton == 1:
            for x in range(sim_settings.speed):
                chain2.check_possible_move(probability)
            chain2_2D.set_alpha(1.)
            chain2_1D.set_alpha(1.)
        else:
            chain2_2D.set_alpha(0.)
            chain2_1D.set_alpha(0.)

    chain1_2D.set_xdata(chain1.xLattice)
    chain1_2D.set_ydata(chain1.yLattice)
    chain1_1D.set_ydata(chain1.yLattice)

    chain2_2D.set_xdata(chain2.xLattice)
    chain2_2D.set_ydata(chain2.yLattice)
    chain2_1D.set_ydata(chain2.yLattice)

    return chain1_2D,chain1_1D,chain2_2D,chain2_1D

#inicjalizacja okna i pól wykresów
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=0, column=1, columnspan=2, rowspan=10,sticky='ewns')
lattice = fig.add_subplot(121)
one_dim_chart = fig.add_subplot(122)
lattice.grid(b=True, dashes=[6,1,2,1])

#inicjalizacja łańcuchów
chain1_2D, = lattice.plot(chain1.xLattice, chain1.yLattice, marker='o',color='b')
chain2_2D, = lattice.plot(chain2.xLattice, chain2.yLattice, marker='o',color='r')
chain1_1D, = one_dim_chart.plot(chain1.x, chain1.yLattice, marker='o',color='b')
chain2_1D, = one_dim_chart.plot(chain2.x, chain2.yLattice, marker='o',color='r')
chain2_2D.set_alpha(0.)
chain2_1D.set_alpha(0.)
ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=10, blit=False)

#ustawienia osi oraz podziałki
lattice.axis([-20,40,-20,40])
one_dim_chart.axis([0,sim_settings.chain2_len+1,-3,20])
start, end = lattice.get_xlim()
lattice.xaxis.set_ticks(np.arange(start, end, 1.))
start, end = lattice.get_ylim()
lattice.yaxis.set_ticks(np.arange(start, end, 1.))
lattice.axes.xaxis.set_ticklabels([])
lattice.axes.yaxis.set_ticklabels([])
one_dim_chart.axes.yaxis.set_ticklabels([])

#RESET BUTTON

def RESET():
    chain1.reset()
    chain2.reset()
button_reset = Tk.Button(root,text="Reset",command=RESET,width=15)
button_reset.grid(column=0,row=5,sticky='nw')



root.mainloop()
