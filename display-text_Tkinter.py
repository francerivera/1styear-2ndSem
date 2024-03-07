from tkinter import *

root = Tk()
root.title("J1T-midLA1")
root.geometry('500x200')

def GUI():
    def display():
        value = E1.get()
        msg.config(text=value)


    frame1 = Frame(root)
    frame1.pack(anchor=N)
    L1 = Label(frame1, text="France Raphael R. RIvera", padx=10)
    L1.pack()
    L2 = Label(frame1, text="Input Text Here", padx=10)
    L2.pack()

    frame2 = Frame(root)
    frame2.pack(padx=10, pady=10, anchor=N)
    E1 = Entry(frame2, bd=5, relief=SUNKEN)
    E1.pack()

    frame3 = Frame(root)
    frame3.pack(side=TOP)
    b1 = Button(frame3, text='Display Text',command=display)
    b1.pack()

    frame4 = Frame(root)
    frame4.pack(anchor=N)
    L3 = Label(frame4, text = "Display", padx= 10, pady=10)
    L3.pack()

    frame5 = Frame(root)
    frame5.pack(anchor=S)
    msg = Label(frame5, text=" ", wraplength=300, padx= 10, pady=10)
    msg.pack()



GUI()
root.mainloop()


****************************

    
import tkinter as tk
from tkinter import ttk
import re


class MainWindows(tk.Tk):

    def __init__(self):
        super().__init__()

        self.frame_main = ttk.Frame(self)

        self.button_display = ttk.Button(self.frame_main, text="Display Text")

        self.label_text = ttk.Label(self.frame_main, text="Hello!")



        self.frame_main.pack(fill=tk.BOTH, expand=True)
        self.button_display.pack()
        self.label_text.pack()


    def get_words_btn(self):
        pass





if __name__ == "__main__":
    main_window = MainWindows()
    main_window.mainloop()