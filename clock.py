from tkinter import *
from tkinter.ttk import*

from time import strftime

root = Tk()
root.title("Clock")


def stime():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, stime)


label = Label(root, font=("Ubuntu, 80"), background="black", foreground="cyan")
label.pack(anchor='center')
stime()

mainloop()
