# Step-----1------Installations the necessary modules
# Step-----2------Import Libraries needed in the project
from tkinter import *
from pytube import YouTube
# Step-----3------Create the API windows or frame
root=Tk()
root.geometry("600x350")
root.resizable(0,0)
root.config(bg="gray")
root.title("Youtube Video Downloader App")
# Step-----4------Create the text and link entry widgets 
Label(root,text="Download any Youtube video", font='Arial 14 bold').place(x=100,y=20)
Label(root,text="Paste the video link here", font='Arial 14',bg='gray',fg='lightgreen').place(x=120,y=50)
# entery widget
videoLink=StringVar()
Entry(root,width=80,textvariable=videoLink).place(x=30,y=85)
# Step-----5------Creating the download function
def downloadVideo():
    url=YouTube(str(videoLink.get()))
    videoStream=url.streams.first()
    videoStream.download()
    Label(root,text="Download Completed Successfully", font='Arial 14 bold',bg='green',fg='white').place(x=120,y=180)

# Step-----6------Create the download button
Button(root,text="Download Now",font='Arial 16 bold',bg='green', padx=1,command=downloadVideo).place(x=100,y=120)


root.mainloop()
