# coding=utf-8
from tkinter import Canvas, Button, Scale, Checkbutton, PhotoImage

class Params():
    """Class containing simulation parameters such as chain length, speed or else"""
    def __init__(self):
        #Crucial simulation parameters
        self.field = .2
        self.speed = 50
        self.chain1_len = 5
        self.chain2_len = 12
        #window resolution
        self.width = 1280
        self.height = 720

class GUI():
    """User interface class"""
    def __init__(self,root,params):
        """Initialization of simulation GUI"""
        #image loading
        self.button_size = 100
        self.stop_png = PhotoImage(file="stop.png")
        self.start_png = PhotoImage(file="start.png")
        self.boost_png = PhotoImage(file="boost.png")
        self.reset_png = PhotoImage(file="reset.png")
        self.exit_png = PhotoImage(file="exit.png")
        #window creating
        self.root = root
        root.title('Repton model for gel electrophoresis')
        root.state('zoomed')
        self.canvas = Canvas(root,width = root.winfo_screenwidth(),height = root.winfo_screenheight())
        self.canvas.grid(row=0, column=1, columnspan=2, rowspan=70,sticky='ewns')
        self.stop_param=True
        self.speed = params.speed

        #grid drawing
        for i in range (110):
            self.canvas.create_line(0,i*30,i*30,0)
            self.canvas.create_line(0,params.width-30*i,30*i,params.width)

        #Simulation buttons
        self.button_quit = Button(root,image=self.exit_png,command=quit,width=self.button_size,height=self.button_size)
        self.button_start_stop_sim = Button(root,image=self.start_png,command=self.start_stop_sim,width=self.button_size, height=self.button_size)
        self.button_boost = Button(root,image=self.boost_png,command=self.boost,width=self.button_size, height=self.button_size)

        #electric field slider
        self.slider_field = Scale(root, from_=0, to=1, resolution=0.05,orient='horizontal',label="Field E:",command=self.field_change,width=15,sliderlength=20)
        self.slider_field.set(0.2)

        #simulation speed slider
        self.slider_speed = Scale(root, from_=10, to=100, resolution=10,orient='horizontal',label="Speed:",command=self.speed_change,width=15,sliderlength=20)
        self.slider_speed.set(self.speed)

        #checkbox for aditional chain
        self.variable_chain_2_checkbutton = 0
        self.checkbutton_chain_2 = Checkbutton(root,text="Chain #2",variable=self.variable_chain_2_checkbutton,command=self.add_chain_2,width=10)

        #adding all tools to window screen
        self.slider_field.grid(column=0,row=0,sticky='nw')
        self.slider_speed.grid(column=0,row=1,pady=0,sticky='nw')
        self.checkbutton_chain_2.grid(column=0,row=2,pady=0,sticky='nw')
        self.button_start_stop_sim.grid(column=0,row=3,pady=0,sticky='nw')
        self.button_boost.grid(column=0,row=5,pady=0,sticky='nw')
        self.button_quit.grid(column=0,row=6,pady=0,sticky='nw')

    #button functions
    def start_stop_sim(self):
        if self.stop_param:
            self.stop_param = False
            self.button_start_stop_sim.config(image=self.stop_png)
        else:
            self.stop_param = True
            self.button_start_stop_sim.config(image=self.start_png)
    def add_chain_2(self):
        if self.variable_chain_2_checkbutton == 1:
            self.variable_chain_2_checkbutton = 0
        else:
            self.variable_chain_2_checkbutton = 1
    def field_change(self,root):
        self.field = self.slider_field.get()
    def speed_change(self,root):
        self.speed = self.slider_speed.get()
    def boost(self):
        self.speed = 100
        self.field = 0.5
        self.slider_field.set(0.5)
        self.slider_speed.set(100)