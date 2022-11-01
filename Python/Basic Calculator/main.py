import tkinter

expression=""
def press(num):
    global expression
    expression = expression + str(num)
    command.set(expression)
 
def equalpress():
     try:
          global expression
          total=str(eval(expression))
          command.set(total)
          expression=""
     except:
          command.set("error")
          expression=""

def clear():
     global expression
     expression =""
     command.set("")
top=tkinter.Tk()
top.title("Calculator")
top.tk_focusFollowsMouse()
top.geometry('300x300')

command=tkinter.StringVar()
display=tkinter.Entry(top,textvariable=command)
display.grid(columnspan=4,ipadx=80)
button1 = tkinter.Button(top, text=' 1 ', fg='black', bg='white',
                    command=lambda: press(1), height=3, width=6)
button1.grid(row=2, column=0)

button2 = tkinter.Button(top, text=' 2 ', fg='black', bg='white',
               command=lambda: press(2), height=3, width=6)
button2.grid(row=2, column=1)

button3 = tkinter.Button(top, text=' 3 ', fg='black', bg='white',
               command=lambda: press(3), height=3, width=6)
button3.grid(row=2, column=2)

button4 = tkinter.Button(top, text=' 4 ', fg='black', bg='white',
               command=lambda: press(4), height=3, width=6)
button4.grid(row=3, column=0)

button5 = tkinter.Button(top, text=' 5 ', fg='black', bg='white',
               command=lambda: press(5), height=3, width=6)
button5.grid(row=3, column=1)

button6 = tkinter.Button(top, text=' 6 ', fg='black', bg='white',
               command=lambda: press(6), height=3, width=6)
button6.grid(row=3, column=2)

button7 = tkinter.Button(top, text=' 7 ', fg='black', bg='white',
               command=lambda: press(7), height=3, width=6)
button7.grid(row=4, column=0)

button8 = tkinter.Button(top, text=' 8 ', fg='black', bg='white',
               command=lambda: press(8), height=3, width=6)
button8.grid(row=4, column=1)

button9 = tkinter.Button(top, text=' 9 ', fg='black', bg='white',
               command=lambda: press(9), height=3, width=6)
button9.grid(row=4, column=2)

button0 = tkinter.Button(top, text=' 0 ', fg='black', bg='white',
               command=lambda: press(0), height=3, width=6)
button0.grid(row=5, column=0)

plus = tkinter.Button(top, text=' + ', fg='black', bg='white',command=lambda: press("+"), height=3, width=9)
plus.grid(row=2, column=3)

minus = tkinter.Button(top, text=' - ', fg='black', bg='white',command=lambda: press("-"), height=3, width=9)
minus.grid(row=3, column=3)

multiply = tkinter.Button(top, text=' * ', fg='black', bg='white',command=lambda: press("*"), height=3, width=9)
multiply.grid(row=4, column=3)

divide = tkinter.Button(top, text=' / ', fg='black', bg='white',command=lambda: press("/"), height=3, width=9)
divide.grid(row=5, column=3)

equal = tkinter.Button(top, text=' = ', fg='black', bg='red',command=equalpress, height=3, width=6)
equal.grid(row=5, column=2)

clear = tkinter.Button(top, text='Clear', fg='black', bg='yellow',command=clear, height=3, width=6)
clear.grid(row=5, column=1)

Decimal=tkinter.Button(top, text='.', fg='black', bg='white',command=lambda: press('.'), height=3, width=6)
Decimal.grid(row=6, column=0)

top.mainloop()