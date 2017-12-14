# coding=utf-8
import tkinter as Tk

class Settings():
    """Klasa przeznaczona do przechowywania wszystkich ustawin programu"""

    def __init__(self,root):
        """Inicjalizacja ustawien symulacji"""
        #Kluczowe parametry symulacji
        self.field = .2
        self.speed = 100
        self.chain1_len = 6
        self.chain2_len = 12
        self.stop_param=True
        #tworzenie okna

        self.root = root
        root.title('Repton model for gel electrophoresis')

        #Przyciski do obsługi symulacji
        self.button_quit = Tk.Button(root,text="Quit",command=quit,width=15)
        self.button_stop_sim = Tk.Button(root,text="Stop",command=self.stop_sim,width=15)
        self.button_start_sim = Tk.Button(root,text="Start",command=self.start_sim,width=15)

        #slider manipulujący polem elektrycznym
        self.slider_field = Tk.Scale(root, from_=0, to=1, resolution=0.05,orient='horizontal',label="Field E:",command=self.field_change,width=15)
        self.slider_field.set(0.2)

        #slider manipulujacy predkoscia
        self.slider_speed = Tk.Scale(root, from_=0, to=300, resolution=30,orient='horizontal',label="Speed:",command=self.speed_change,width=15)
        self.slider_speed.set(30)

        #checkbox dodający kolejny łańcuch
        self.variable_chain_2_checkbutton = Tk.IntVar()
        self.variable_chain_2_checkbutton = 0
        self.checkbutton_chain_2 = Tk.Checkbutton(root,text="Chain #2",variable=self.variable_chain_2_checkbutton,command=self.add_chain_2,width=10)

        #dodanie wszystkich elementów do okna w odpowiednich miejscach
        self.slider_field.grid(column=0,row=0,sticky='nw')
        self.slider_speed.grid(column=0,row=1,pady=5,sticky='nw')
        self.checkbutton_chain_2.grid(column=0,row=2,pady=5,sticky='nw')
        self.button_start_sim.grid(column=0,row=3,pady=5,sticky='nw')
        self.button_stop_sim.grid(column=0,row=4,sticky='nw',pady=5)
        self.button_quit.grid(column=0,row=6,pady=5,sticky='nw')

    #funkcje obsługujące przyciski
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

