from tkinter import *

window = Tk()

def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"

def decrease():
    value = int(lbl_value["text"])
    if value > 0:
        lbl_value["text"] = f"{value - 1}"



btn_decrease = Button(master=window, text="-", command=decrease)
btn_decrease.grid(row=0, column=1, sticky="nsew")


lbl_value = Label(master=window, text="0")
lbl_value.grid(row=0, column=2)

btn_increase = Button(master=window, text="+", command=increase)
btn_increase.grid(row=0, column=3, sticky="nsew")

window.mainloop()

##############



