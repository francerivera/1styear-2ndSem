from tkinter import *
from tkinter.messagebox import showinfo

def GUI():
    def Choices(value):
        print(f"You selected: {value}")

    root = Tk()
    root.title("J1T-midLA2")
    root.geometry("700x300")

    name_text = Label(root, text="Rivera's Car Maintenance App", font=('Arial', 25, 'bold'),
                        bg='#48D5E7', fg='white', bd=12, relief=FLAT)
    name_text.pack(fill=X)


    car = IntVar()

    values = {"BMW             5,000.00": 5000.00,
              "Subaru          2,000.00": 2000.00,
              "Chevrolet     4,100.00": 4100.00}


    w_values = {}
    values2 = {"Leather   550.00": 550.00,
               "GPS         1000.00": 1000.00}


    x = IntVar()

    values3 = {"Hard Top": "Hard Top",
               "Convertible": "Convertible"}


    y_values = {}
    values4 = {"Wheel Upgrade                  550.00": 550.00,
               "Performance Package      1000.00": 1000.00}

    ParentFrame=Frame(root)
    ParentFrame.pack(pady=20)

    CarFrame=Frame(ParentFrame)
    CarFrame.grid(row=0, column=0)

    for i, (text, value) in enumerate(values.items(), start=1):
        radio_button = Radiobutton(CarFrame, text=text, variable=car, value=value, command=lambda car=value: Choices(car))
        radio_button.grid(row=i, column=0, padx=10, sticky='W')

    for i, (text, value) in enumerate(values2.items(), start=1):
        w_values[value] = BooleanVar()
        check_button = Checkbutton(CarFrame, text=text, variable=w_values[value], onvalue=value, offvalue=0, command=lambda value=value: Choices(value))
        check_button.grid(row=i, column=1, padx=10, sticky='W')

    for i, (text, value) in enumerate(values3.items(), start=1):
        radio_button = Radiobutton(CarFrame, text=text, variable=x, value=value, command=lambda x=value: Choices(x))
        radio_button.grid(row=i, column=2, padx=10, sticky='W')

    for i, (text, value) in enumerate(values4.items(), start=1):
        y_values[value] = BooleanVar()
        check_button = Checkbutton(CarFrame, text=text, variable=y_values[value], onvalue=value, offvalue=0, command=lambda value=value: Choices(value))
        check_button.grid(row=i, column=3, padx=10, sticky='W')

    root.mainloop()

GUI()

