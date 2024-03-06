from tkinter import *

root = Tk()
root.title("J1T-midLA1")
root.geometry('300x100')

def GUI():
    def display():
        value = E1.get()
        msg.config(text=value)

    main_frame = Frame(root)

    frame1 = Frame(main_frame)
    frame1.pack(anchor=NW)
    L1 = Label(frame1, text="France Raphael R. RIvera", padx=10)
    L1.pack()

    frame2 = Frame(root)
    frame2.pack(padx=10, anchor=NW)
    E1 = Entry(frame2, bd=5)
    E1.pack()

    frame3 = Frame(root)
    frame3.pack(side=BOTTOM)
    b1 = Button(frame3, text='Display Text',command=display)
    b1.pack()

    frame4 = Frame(root)
    frame4.pack(anchor=NE)
    L2 = Label(frame4, text = "Display")
    L2.pack()
    msg = Message(frame4, text = " ")
    msg.pack()


GUI()
root.mainloop()
