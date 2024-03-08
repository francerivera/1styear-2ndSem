from tkinter import *

def GUI():
    def display():
        word = entry_text.get()
        if len(word.split()) > 1:
            label_text.config(text="One word only.", fg='red')
        else:
            label_text.config(text=word, wraplength=250, fg='black')

    root = Tk()
    root.title("J1T-midLA1")
    root.geometry('700x400+700+400')
    root.configure(bg='#B8DE8F')


    frame1 = Frame(root)
    frame1.pack(anchor=N, pady=10)
    name_text = Label(frame1, text="France Raphael R. Rivera", font=('Monotype Corsiva', 50, 'bold')
                      ,bg='#800000', fg='gold', bd=12, relief=FLAT)
    name_text.pack()

    frame2 = Frame(root)
    frame2.pack()
    input_text = Label(frame2, text="Input Text Here:", font=('Rockwell', 20, 'bold')
                       ,bg='#800000', fg='white', bd=8, relief=RIDGE)
    input_text.pack()

    frame3 = Frame(root)
    frame3.pack(anchor=N, pady=10)
    entry_text = Entry(frame3, font=('Helvetica', 20), bd=5, relief=SUNKEN, width=36)
    entry_text.pack()

    frame4 = Frame(root)
    frame4.pack(side=TOP, pady=5)
    button_display = Button(frame4, text='Display Text',font=('Arial', 15, 'bold')
                ,bg='#008080', fg='white', bd=8, command=display)
    button_display.pack()

    frame5 = Frame(root)
    frame5.pack(anchor=S, pady=10)
    label_text = Label(frame5, bg='#B8DE8F', padx= 10, pady=10,font=('Helvetica', 25, 'bold'))
    label_text.pack()

    root.mainloop()

GUI()

