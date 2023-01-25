# Step-----1------Install the necessary modules------------done

# Step-----2------Import Libraries needed to make this application
from tkinter import *
from textblob import TextBlob
# Step-----3------Create the API windows or frame
app=Tk()
app.configure(background='greenyellow')
app.geometry("750x350")
app.resizable(0,0)
app.title("Spell Checker and Corrector App")
# Step-----4------Create the text and words entry widgets 
heading_text=Label(app,text="Wellcome to Spell Checcker and Corrector App",font='Arial 16 bold',fg='yellow',bg='black')
lbl_input=Label(app,text="input word here",font='Arial 14 bold', fg='white', bg='magenta')
lbl_corrected=Label(app,text="corrected word",font='Arial 14 bold', fg='white', bg='green')

heading_text.grid(row=0, column=1,pady=20)
lbl_input.grid(row=1, column=0,padx=10)
lbl_corrected.grid(row=3, column=0,padx=10)
# create text entry wedgets here
input_word_box=Entry(app,width=40,font='Arial 14 bold')
corrected_word_box=Entry(app,width=40,font='Arial 14 bold')

input_word_box.grid(row=1, column=1,pady=10)
corrected_word_box.grid(row=3, column=1,pady=10)

# Step-----5------Creating the functions
#create a function to get the corrected words
def spellCorrection():
    word_input=input_word_box.get()
    text=TextBlob(word_input)
    #get the corrected word
    corrected_word=str(text.correct())
    #insert the value in the text entry box
    corrected_word_box.insert(10,corrected_word)
# a function to clear the texts found inside box the entry boxes
def clearAllWords():
    input_word_box.delete(0,END)
    corrected_word_box.delete(0,END)


# Step-----6------Create the buttons
# Create a correction button
btn1=Button(app, text='Correction',font='Arial 14 bold', fg='black', bg='aqua', border=5,command=spellCorrection)
btn1.grid(row=2,column=1)
#Create button that enables to clear the word entred in the entry box
btn1=Button(app, text='Clear All',font='Arial 14 bold', fg='black', bg='red', border=5,command=clearAllWords)
btn1.grid(row=4,column=1)

app.mainloop()
