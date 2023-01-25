from tkinter import *
from translate import Translator

screen = Tk()
screen.title('Translator App')
screen.geometry('450x350')
screen.resizable(0,0)
screen.config(bg='gray')

InputLanguageChoice = StringVar()
InputLanguageChoice.set('English')

LanguageOptions = OptionMenu(screen, InputLanguageChoice, 'English', 'French', 'German', 'Spanish', 'Hindi')
LanguageOptions.config(bg='green', fg='white')
LanguageOptions['menu'].config(bg='lightblue')
LanguageOptions.grid(row=2, column=1, pady=10, ipadx=15)

OutputLanguageChoice = StringVar()
OutputLanguageChoice.set('Chose')

LanguageOptions = OptionMenu(screen, OutputLanguageChoice, 'English', 'French', 'German', 'Spanish', 'Hindi')
LanguageOptions.config(bg='green', fg='white')
LanguageOptions['menu'].config(bg='orange')
LanguageOptions.grid(row=2, column=4, ipadx=15)


Label(screen, text='Type here').grid(row=3, column=1)
TextVar = StringVar()
Textbox = Entry(screen, textvariable=TextVar).grid(row=5, column=1, ipadx=10, ipady=20)

Label(screen, text='Output').grid(row=3, column=4)
OutputVar = StringVar()
Textbox = Entry(screen, textvariable=OutputVar).grid(row=5, column=4, ipadx=10, ipady=20)

def translate():
    translator = Translator(from_lang=InputLanguageChoice.get(), to_lang=OutputLanguageChoice.get())
    translation = translator.translate(TextVar.get())
    OutputVar.set(translation)
    
Button(screen, text='Translate', command=translate, relief=GROOVE).grid(row=8, column=3)
screen.mainloop()