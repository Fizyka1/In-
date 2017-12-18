# coding=utf-8
from tkinter import Canvas, Button, Scale, Checkbutton

class Params():
    """Class containing simulation parameters such as chain length, speed or else"""
    def __init__(self):
        #Crucial simulation parameters
        self.field = .2
        self.speed = 200
        self.chain1_len = 6
        self.chain2_len = 12
        #window resolution
        self.width = 1280
        self.height = 720

class GUI():
    """User interface class"""
    def __init__(self,root,params):
        """Initialization of simulation GUI"""

        #window creating
        self.root = root
        root.title('Repton model for gel electrophoresis')
        self.canvas = Canvas(root,width = params.width,height = params.height)
        self.canvas.grid(row=0, column=1, columnspan=2, rowspan=10,sticky='ewns')
        self.stop_param=True

        #grid drawing
        for i in range (100):
            self.canvas.create_line(0,i*30,i*30,0)
            self.canvas.create_line(0,params.width-30*i,30*i,params.width)

        #Simulation buttons
        self.button_quit = Button(root,text="Quit",command=quit,width=15)
        self.button_stop_sim = Button(root,text="Stop",command=self.stop_sim,width=15)
        self.button_start_sim = Button(root,text="Start",command=self.start_sim,width=15)

        #electric field slider
        self.slider_field = Scale(root, from_=0, to=1, resolution=0.05,orient='horizontal',label="Field E:",command=self.field_change,width=15)
        self.slider_field.set(0.2)

        #simulation speed slider
        self.slider_speed = Scale(root, from_=50, to=300, resolution=50,orient='horizontal',label="Speed:",command=self.speed_change,width=15)
        self.slider_speed.set(params.speed)

        #checkbox for aditional chain
        self.variable_chain_2_checkbutton = 0
        self.checkbutton_chain_2 = Checkbutton(root,text="Chain #2",variable=self.variable_chain_2_checkbutton,command=self.add_chain_2,width=10)

        #adding all tools to window screen
        self.slider_field.grid(column=0,row=0,sticky='nw')
        self.slider_speed.grid(column=0,row=1,pady=5,sticky='nw')
        self.checkbutton_chain_2.grid(column=0,row=2,pady=5,sticky='nw')
        self.button_start_sim.grid(column=0,row=3,pady=5,sticky='nw')
        self.button_stop_sim.grid(column=0,row=4,sticky='nw',pady=5)
        self.button_quit.grid(column=0,row=6,pady=5,sticky='nw')

    #functions for buttons interactions
    def stop_sim(self):
        self.stop_param=True
    def start_sim(self):
        self.stop_param=False
    def add_chain_2(self):
        if self.variable_chain_2_checkbutton == 1:
            self.variable_chain_2_checkbutton = 0
        else:
            self.variable_chain_2_checkbutton = 1
    def field_change(self,root):
        self.field = self.slider_field.get()
    def speed_change(self,root):
        self.speed = self.slider_speed.get()