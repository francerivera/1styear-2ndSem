from tkinter import *

def GUI():

    root = Tk()
    root.title("J1T-midLA2")
    root.geometry("700x300")
    root.configure(bg='#ffa100')

    name_text = Label(root, text="Rivera's Car Maintenance App", font=('Arial', 25, 'bold'),
                        bg='#48D5E7', fg='white', bd=12, relief=FLAT)
    name_text.pack(fill=X)

    car = StringVar()

    car.set(None)

    values = {"BMW             5,000.00": 5000,
              "Subaru          2,000.00": 2000,
              "Chevrolet     4,100.00": 4100}
    interior = []
    in_var1 = IntVar()
    in_var1.set(0)
    in_var2 = IntVar()
    in_var2.set(0)
    interior.append(in_var1)
    interior.append(in_var2)

    values2 = {"Leather                                                                    550.00": 550,
               "GPS         1,000.00": 1000}

    exterior_f = StringVar()
    exterior_f.set(None)
    values3 = {"Hard Top": "Hard Top",
               "Convertible": "Convertible"}

    exterior = []
    ex_var1 = IntVar()
    ex_var1.set(0)
    ex_var2 = IntVar()
    ex_var2.set(0)
    exterior.append(ex_var1)
    exterior.append(ex_var2)

    values4 = {"Wheel Upgrade                                                      550.00": 550,
               "Performance Package                                  1,000.00": 1000}

    ParentFrame=Frame(root)
    ParentFrame.pack(pady=20)

    CarFrame=Frame(ParentFrame)
    CarFrame.grid(row=0, column=0)

    for index, item in enumerate(values):
        radio_button = Radiobutton(CarFrame, text=item, variable=car, value=item)
        radio_button.grid(row=index+1, column=0, padx=10)


    Label(CarFrame, text="Car Brand", font=("Arial", 10, 'bold')).grid(row=0, column=0)
    Label(CarFrame, text="Interior Option", font=("Arial", 10, 'bold')).grid(row=0, column=1)
    Label(CarFrame, text="Exterior Finish", font=("Arial", 10, 'bold')).grid(row=0, column=2)
    Label(CarFrame, text="Exterior Option", font=("Arial", 10, 'bold')).grid(row=0, column=3)
    check_button1 = Checkbutton(CarFrame, text="Leather       550.00", variable=in_var1, onvalue=550, offvalue=0)
    check_button1.grid(row=1, column=1, padx=10, sticky='W')
    check_button2 = Checkbutton(CarFrame, text="GPS            1,000.00", variable=in_var2, onvalue=1000, offvalue=0)
    check_button2.grid(row=2, column=1, padx=10, sticky='W')

    for index, item in enumerate(values3):

        radio_button = Radiobutton(CarFrame, text=item, variable=exterior_f, value=values3[item])
        radio_button.grid(row=index+1, column=2, padx=10, sticky='W')


    check_button1 = Checkbutton(CarFrame, text="Wheel Upgrade                    550.00", variable=ex_var1, onvalue=550, offvalue=0)
    check_button1.grid(row=1, column=3, padx=10, sticky='W')
    check_button2 = Checkbutton(CarFrame, text="Performance Package      1,000.00", variable=ex_var2, onvalue=1000, offvalue=0)
    check_button2.grid(row=2, column=3, padx=10, sticky='W')


    def totality():
        top = Toplevel()
        top.geometry("400x300")
        top.title("Receipt")
        new_interior = list(filter(0 or None, [item.get() for item in interior]))
        new_exterior = list(filter(0 or None, [item.get() for item in exterior]))
        print(new_exterior)
        print(new_interior)
        total_interior = sum(new_interior[i] for i in range(len(new_interior)))
        total_exterior = sum(new_exterior[i] for i in range(len(new_exterior)))
        car.get()
        total = (int(values[car.get()]) + total_interior + total_exterior)
        Label(top, text=f"You selected: {car.get()}",padx=10,pady=10).pack(anchor=W)
        if len(new_interior) > 1:
            interior_text = f"You selected: {list(values2.keys())[list(values2.values()).index(new_interior[0])]} and {list(values2.keys())[list(values2.values()).index(new_interior[1])]}"
        elif len(new_interior) == 1:
            interior_text = f"You selected: {list(values2.keys())[list(values2.values()).index(new_interior[0])]}"
        else:
            interior_text = "You selected: N/A"
        Label(top, text=interior_text, padx=10,pady=10).pack(anchor=W)

        if exterior_f.get():
            exterior_finish_text = f"You selected: {exterior_f.get()}"
        else:
            exterior_finish_text = "You selected: N/A"
        Label(top, text=exterior_finish_text, padx=10,pady=10).pack(anchor=W)

        if len(new_exterior) > 1:
            exterior_option_text = f"You selected: {list(values4.keys())[list(values4.values()).index(new_exterior[0])]}\n{list(values4.keys())[list(values4.values()).index(new_exterior[1])]}"
        elif len(new_exterior) == 1:
            exterior_option_text = f"You selected: {list(values4.keys())[list(values4.values()).index(new_exterior[0])]}"
        else:
            exterior_option_text = "You selected: N/A"
        Label(top, text=exterior_option_text, padx=10,pady=10).pack(anchor=W)
        Label(top, text="________________________________________________________________________").pack()
        Label(top, text=f"Total Amount: {total}", font=('Arial', 15, 'bold'),padx=30,pady=10).pack(anchor=E)

    confirm = Button(root, text="Purchase", font=('Arial', 15, 'bold'), bd=8, relief=GROOVE, command= totality)
    confirm.pack()


    root.mainloop()

GUI()

