import Data_Input
import tkinter
import csv
import matplotlib.pyplot as plt
import numpy as np

#Closing Window Function
def close_win():
   top.destroy()

#Curve Fitting Function
def pull(ch):
    n = 0
    X = 0
    Y = 0
    sum_of_y = 0
    sum_of_x = 0
    sum_of_xsquare = 0
    sum_of_xy = 0
    sum_of_xcube = 0
    sum_of_xquad = 0
    sum_of_yxsquare = 0
    choice = ch
    f = open(r"Curve Fitting Script\data.csv")
    text = csv.reader(f)
    for i in text:
        if (i == []):
            break
        sum_of_x += float(i[0])
        sum_of_y += float(i[1])
        sum_of_xy += (float(i[0]) * float(i[1]))
        sum_of_xsquare += float(i[0])**2
        sum_of_xcube += float(i[0])**3
        sum_of_xquad += float(i[0])**4
        sum_of_yxsquare += (float(i[0])**2) * float(i[1])
        n += 1
        next(text)
    if (choice == 1):
        a = round(((n * sum_of_xy) - (sum_of_y * sum_of_x)) /
                  (n * sum_of_xsquare - (sum_of_x**2)), 3)
        b = round(
            ((sum_of_y - ((n * sum_of_xy - (sum_of_x * sum_of_y)) /
                          (n * sum_of_xsquare - sum_of_x**2) * sum_of_x)) / n),
            3)
        if (b < 0):
            plt.title("y=({})x+({})".format(a, b))
            Y = a
            X = -b / a
        else:
            Y = b
            X = -a / b
            plt.title("y=({})x+({})".format(b, a))
        xpoints = np.array([0, X])
        ypoints = np.array([0, Y])
        plt.plot(xpoints, ypoints)
        plt.show()
    elif (choice == 2):
        A = np.array([[n, sum_of_x, sum_of_xsquare],
                      [sum_of_x, sum_of_xsquare, sum_of_xcube],
                      [sum_of_xsquare, sum_of_xcube, sum_of_xquad]])
        B = np.array([sum_of_y, sum_of_xy, sum_of_yxsquare])
        try:
            C = np.linalg.solve(A, B)
            plt.title("y=({:.2f})x^2+({:.2f})x+({:.2f})".format(
                C[0], C[1], C[2]))
            x = np.linspace(-10, 10, 100)
            y = C[0] * x**2 + C[1] * x + C[2]
            plt.plot(x, y)
            plt.show()
        except:
            print("Singular Error ")
            plt.show()
    plt.clf()


#Main Function
top = tkinter.Tk()
top.title("CURVE FITTING")
top.tk_focusFollowsMouse()
top.geometry("300x160")
one = tkinter.Button(top,
                     text="Straight Line",
                     command=lambda: pull(1),
                     height=8,
                     width=12,bg='green')
one.grid(row=1, column=1)
two = tkinter.Button(top,
                     text="Parabola",
                     command=lambda: pull(2),
                     height=8,
                     width=12,bg='blue')
two.grid(row=1, column=2)                     
exitbutton = tkinter.Button(top,
                            text="EXIT",
                            command=lambda:close_win(),
                            height=8,
                            width=12,bg='red')
exitbutton.grid(row=1,column=3)
top.mainloop()
top.destroy()