import sqlite3
import tkinter as tk
from tkinter import messagebox

def create_table(conn):
  cursor = conn.cursor()
  cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                  id INTEGER PRIMARY KEY,
                  name TEXT,
                  age INTEGER
                  )''')
  conn.commmit()

def insert_user(conn, name, age):
  cursor = conn.cursor()
  cursor.execute("INSERT INTO users (name, age) VALUES (?,?)", (name, age))
  conn.commit()

def fetch_all_users(conn):
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM users")
  users = cursor.fetchall()
  return users

def update_user_age(conn, name, new_age):
  cursor = conn.cursor()
  cursor.execute("UPDATE users SET age = ? WHERE name = ?", (new_age, name))
  conn.commit()

def add_user():
  name = name_entry.get()
  age = int(age_entry.get()

  if name and age:
    insert user(conn, name, age)
    messagebox.showinfo("Success", "User added successfully!")
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
  else:
    messagebox.showerror("Error", "Please enter both name and age.")

def update_age():
  name = name_entry.get()
  new_age = int(age_entry.get())

  if name and new_age:
    update user age(conn, name, new_age)
    messagebox.showinfo("Success", "User's age updated successfully!")
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
  else:
    messagebox.showerror("Error", "Please enter both name and new age.")

def show_users():
  users=fetch_all_users(conn)
  if users:
    users_list_delete(0, tk.END)
    for user in users:
      user_list.insert(tk.END, user)
  else:
    messagebox.showinfo("Info", "No users found.")

def exit_app():
  conn.close()
  root.destroy()

conn = sqlite3.connect('inventory.db')
create_table(conn)

root = tk.Tk()
root.title("User Database")

name_label = tk.Label(rootm text="Name")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

age_label = tk.Label(root, text="Age")
age_label.grid(row=1, column=0, padx=5, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=5, pady=5)

add_button = tk.Button(root, text="Add User", command=add_user)
add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

update_button = tk.Button(root, text="Update Age", command=update_age)
update_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

show_button = tk.Button(root, text="Show Users", command=show_users)
show_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

user_list = tk.Listbox(roow, width=50)
user_list.grid(row=5, column=0, columspan=2, padx=5, pady=5)

exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

root.mainloop()



