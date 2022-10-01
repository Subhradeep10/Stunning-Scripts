# importing tkinter
from tkinter import *
# importing YouTube module
from pytube import YouTube
# initializing tkinter
root = Tk()
# setting the geometry of the GUI
root.geometry("400x350")
# setting the title of the GUI
root.title("Youtube video downloader application")
# defining download function
def download():
    # using try and except to execute program without errors
    try:
        myVar.set("Downloading...")
        root.update()
        YouTube(link.get()).streams.first().download()
        link.set("Video downloaded successfully")
    except Exception as e:
        myVar.set("Mistake")
        root.update()
        link.set("Enter correct link")

# created the Label widget to welcome user
Label(root, text="Welcome to youtube\nDownloader Application", font="Consolas 15 bold").pack()
# declaring StringVar type variable
myVar = StringVar()
# setting the default text to myVar
myVar.set("Enter the link below")
# created the Entry widget to ask user to enter the url
Entry(root, textvariable=myVar, width=40).pack(pady=10)
# declaring StringVar type variable
link = StringVar()
# created the Entry widget to get the link
Entry(root, textvariable=link, width=40).pack(pady=10)
# created and called the download function to download video
Button(root, text="Download video", command=download).pack()
# running the mainloop
root.mainloop()