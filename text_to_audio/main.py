import pyttsx3
import os
# for converting a text 
voice = pyttsx3.init()
myText="hello my beautiful people. now, in this video you are learning how you can convert text to speech using python"
voice.say(myText)
voice.save_to_file(myText, "text.mp3")
voice.runAndWait()
os.system("start hello1.mp3")

#-----------for convering any text word or pdf file in to audio----------------
# myFile = open("hello.txt","r")
# myText = myFile.read()
# voice = pyttsx3.init()
# voice.say(myText)
# voice.save_to_file(myText, "python.mp3")
# voice.runAndWait()
# os.system("start python.mp3")



