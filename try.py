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

from tkinter import *

root = Tk()

def toggle():
    if check_var.get():
        label.config(text="Feature Enabled")
    else:
        label.config(text="Feature Disabled")


check_var = BooleanVar()
checkbutton = Checkbutton(root, text="Enable Feature", variable=check_var, command=toggle)
checkbutton.pack()

label = Label(root, text="Feature Disabled ")
label.pack()

root.mainloop()

#################

from tkinter import *
from tkinter.messagebox import showinfo


root = Tk()
root.geometry("500x300")
root.resizable(False, False)
root.title("Radio Button Demo")


def show_selected_size():
    showinfo(title='Result', message=selected_size.get())

selected_size = StringVar()
sizes = (("Small","S"),("Medium", "M"),("Large","L"),("Extra Large","XL"))

label = Label(text="What's your size?")
label.pack(fill="x", padx=6, pady=6)

for size in sizes:
    r = Radiobutton(root, text=size[0], value=size[1], variable=selected_size)
    r.pack(fill="x", padx=6, pady=6)

button = Button(root, text="Get Selected Size", command=show_selected_size)
button.pack(fill="x", padx=6, pady=6)


############

def item_click():
    print("Menu item clicked!")


menu = Menu(root)

menu.add_command(label="tao", command=item_click)
menu.add_command(label="bagay", command=item_click)
menu.add_command(label="hayop", command=item_click)

submenu = Menu(menu)
submenu.add_command(label="France", command=item_click)
submenu.add_command(label="Rivera", command=item_click)

menu.add_cascade(label="Submenu", menu=submenu)

root.config(menu=menu)

root.mainloop()


asd
