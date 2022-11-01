import tkinter
from weather import show_weather

def push():
    str=e.get()
    if str!='':
        result=show_weather(str)
        label_two.config(text="The Weather Details are as follows:")
        label.config(text=result)
top=tkinter.Tk()
top.title('WEATHER APP')
top.tk_focusFollowsMouse()

# Setting the window size
top.geometry('400x300')

# Adding the Label for Text Display
label_one=tkinter.Label(top,text="Enter Name of the Place",width=20)
label_one.pack()

# Adding the Entry 
e=tkinter.Entry(top)
e.focus_set()
e.pack()

# Adding the button 
button=tkinter.Button(top,text="Get Weather",width=20,height=2,command=push,bg='#ffffff', activebackground='#00ff00').pack(pady=20)

# Adding the button for displaying captions
label_two=tkinter.Label(top,text="")
label_two.pack()


# Adding the Label for Weather Display
label=tkinter.Label(top,text="")
label.pack()

top.mainloop()