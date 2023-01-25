from tkinter import *
from time import strftime
root=Tk()
root.title("Digital Clock")

def time():
    timeFormat = strftime('%H:%M:%S %p')
    clock.config(text = timeFormat)
    clock.after(1000, time)

clock=Label(root, font="Arial 100 bold", pady=30, fg="cyan", bg="black")
clock.pack(anchor="center")

time()
mainloop()