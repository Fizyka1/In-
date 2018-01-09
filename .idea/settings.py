# coding=utf-8
from tkinter import Canvas, Button, Scale, Checkbutton, PhotoImage, Frame
from sys import platform

class Params():
    """Class containing simulation parameters such as chain length, speed or else"""
    def __init__(self):
        #Crucial simulation parameters
        self.field = .2
        self.speed = 50
        self.chain1_len = 7
        self.chain2_len = 20
        #window resolution
        self.width = 1280
        self.height = 720

class GUI():
    """User interface class"""
    def __init__(self,root,params):
        """Initialization of simulation GUI"""
        #params init
        self.stop_param=True
        self.speed = params.speed
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

        #maximizing window despite operating system
        if platform == 'linux' or platform == 'linux2':
            root.attributes('-zoomed', True)
        elif platform == 'win32':
            root.state('zoomed')
        else:
            print('Nie rozpoznaję systemu')
        #creating frames and GUI
        self.frame_left = Frame(root, borderwidth = 0, relief = 'groove')
        self.frame_right = Frame(root, borderwidth = 5, relief = 'ridge')
        self.frame_left_up = Frame(self.frame_left, borderwidth = 0, relief = 'groove')
        self.frame_left_up_upper = Frame(self.frame_left_up, borderwidth = 0, relief = 'groove')
        self.frame_left_up_lower = Frame(self.frame_left_up, borderwidth = 0, relief = 'groove')
        self.frame_left_down = Frame(self.frame_left, borderwidth = 5, relief = 'ridge')
        self.canvas = Canvas(self.frame_right, width = root.winfo_screenwidth(),height = root.winfo_screenheight())
        self.canvas1D = Canvas(self.frame_left_down, height = 1200)
        #major frames
        self.frame_left.pack(side='left',expand=True)
        self.frame_right.pack(side='right',expand = True)
        self.frame_left_up.pack(expand = True, fill = 'both')
        self.frame_left_down.pack(expand = True, fill = 'both')
        self.frame_left_up_upper.pack(expand = True, fill = 'both')
        self.frame_left_up_lower.pack(expand = True, fill = 'both')

        #grid drawing on canvas
        for i in range (110):
            self.canvas.create_line(0,i*30,i*30,0)
            self.canvas.create_line(0,params.width-30*i,30*i,params.width)

        #Simulation buttons
        self.button_quit = Button(self.frame_left_up_lower,image=self.exit_png,command=quit,width=self.button_size,height=self.button_size)
        self.button_start_stop_sim = Button(self.frame_left_up_lower,image=self.start_png,command=self.start_stop_sim,width=self.button_size, height=self.button_size)
        self.button_boost = Button(self.frame_left_up_lower,image=self.boost_png,command=self.boost,width=self.button_size, height=self.button_size)

        #electric field slider
        self.slider_field = Scale(self.frame_left_up_upper, from_=0, to=1, resolution=0.05,orient='horizontal',label="Field E:",command=self.field_change,width=15,sliderlength=30, length = 140)
        self.slider_field.set(0.2)

        #simulation speed slider
        self.slider_speed = Scale(self.frame_left_up_upper, from_=10, to=100, resolution=10,orient='horizontal',label="Speed:",command=self.speed_change,width=15,sliderlength=30, length = 140)
        self.slider_speed.set(self.speed)

        #checkbox for aditional chain
        self.variable_chain_2_checkbutton = 0
        self.checkbutton_chain_2 = Checkbutton(self.frame_left_up_upper,text="Chain #2",variable=self.variable_chain_2_checkbutton,command=self.add_chain_2,width=15,height=2)

        #packing all elements
        self.slider_field.pack(side='left')
        self.slider_speed.pack(side='left')
        self.checkbutton_chain_2.pack(side='left')
        self.button_start_stop_sim.pack(side='right')
        self.button_boost.pack(side='right')
        self.button_quit.pack(side='left')
        self.canvas.pack(fill='both')
        self.canvas1D.pack(fill='both')


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