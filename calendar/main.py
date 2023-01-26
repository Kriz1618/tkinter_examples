from tkinter import *
from tkcalendar import Calendar

app = Tk()
app.geometry('420x420')
app.title('Calendar Date Picker')
app.config(bg='darkblue')

calendarObj = Calendar(app, selectmode='day', year=2023, month=1, date=23)

calendarObj.pack(pady=45)

def fetch_date():
    date.config(text="Selected Date: " + calendarObj.get_date())
    
Button(app, text='Select Date', bg='black', fg='white', command=fetch_date).pack()

date = Label(app, text='', bg='black', fg='white')
date.pack(pady=20)


app.mainloop()