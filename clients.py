import tkinter as tk
from tkinter import *
import login
import face
import create

root = tk.Tk(className=" Client Management", useTk=1)
root.resizable(0,0)
canvas1 = tk.Canvas(root, width=500, height=300)
canvas1.pack()

label1 = tk.Label(root, text="Welcome to Client Database")
label1.config(font=('verdana', 18))
canvas1.create_window(250, 30, window=label1)

button = tk.Button(root, text="Create User", command=create)
button.config(font=('verdana', 10, 'bold'))
canvas1.create_window(250, 100, window=button)

button1 = tk.Button(root, text="Log In", command=login)
button1.config(font=('verdana', 8, 'bold'))
canvas1.create_window(166, 180, window=button1)

button2 = tk.Button(root, text="Face ID", command=face)
button2.config(font=('verdana', 8, 'bold'))
canvas1.create_window(333, 180, window=button2)

button3 = tk.Button(root, text="Exit", command=root.destroy)
button3.config(bg='Red', fg='white', font=('verdana', 10, 'bold'))
canvas1.create_window(250, 260, window=button3)

root.mainloop()