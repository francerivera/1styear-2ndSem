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
  
asd
