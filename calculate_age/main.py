from tkinter import *
import datetime
from PIL import Image, ImageTk

root = Tk()
root.geometry('580x720')
root.title('Age Calculator App')
root.resizable(0,0)

name = Label(root, text='Name:')
name.place(x=150, y=300)
year = Label(root, text='Year:')
year.place(x=150, y=350)
month = Label(root, text='Month:')
month.place(x=150, y=400)
day = Label(root, text='Day:')
day.place(x=150, y=450)

nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

nameEntry = Entry(root, textvariable=nameValue, width=25, font='Arial 14')
nameEntry.place(x=200,  y=300)
yearEntry = Entry(root, textvariable=yearValue, width=25, font='Arial 14')
yearEntry.place(x=200,  y=350)
monthEntry = Entry(root, textvariable=monthValue, width=25, font='Arial 14')
monthEntry.place(x=200,  y=400)
dayEntry = Entry(root, textvariable=dayValue, width=25, font='Arial 14')
dayEntry.place(x=200,  y=450)

def userInput():
    name = nameEntry.get()
    hero = Person(name, datetime.date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get())))
    textArea = Text(master=root, height=2, width=25, bg='black', fg='green', font='Arial 12 bold')
    textArea.place(x=200, y=570)
    response = "Hi {hero}!!, you are {age} years old.".format(hero=name, age=hero.age())
    textArea.insert(END, response)

class Person:
    def __init__(selft, name, birthday):
        selft.name = name
        selft.birthday = birthday
    
    def age(selft):
        today = datetime.date.today()
        age = today.year - selft.birthday.year
        return age

image = Image.open('age.jpg') 
image.thumbnail((500, 200), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
image_label = Label(image=photo)

Button(root, text='Calculate Age', bg='orange', font='Arial 14 bold', command=userInput).place(x=220, y=520)


root.mainloop()
