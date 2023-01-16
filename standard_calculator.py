from tkinter import *
window = Tk()

# add widgets from here
window.geometry("235x260+760+400")
window.title("Calculator")


# entry widget
textbox = Frame(window, bd = 2, height = 10, width= 10)
textbox.place(x=100, y= 100)

# label widget
zero = Label(window, text="0", font=("Nexa", 25))
zero.place(x=210, y=20)

# button widget
# first row (left to right)
mc = Button(window, text="MC", font=("Nexa", 10), bd=2, height= 1, width=4, fg="darkblue")
mc.place(x=3, y=80)
mr = Button(window, text="MR", font=("Nexa", 10), bd=2, height= 1, width=4, fg="darkblue")
mr.place(x=50, y=80)
ms = Button(window, text="MS", font=("Nexa", 10), bd=2, height= 1, width=4, fg="darkblue")
ms.place(x=97, y=80)
mplus = Button(window, text="M+", font=("Nexa", 10), bd=2, height= 1, width=4, fg="darkblue")
mplus.place(x=144, y=80)
mminus = Button(window, text="M-", font=("Nexa", 10), bd=2, height= 1, width=4, fg="darkblue")
mminus.place(x=191, y=80)

# second row (left to right)
backspace = Button(window, text="<-", font=("Nexa", 10), bd=2, height= 1, width=4)
backspace.place(x=3, y=110)
ce = Button(window, text="CE", font=("Nexa", 10), bd=2, height=1, width=4)
ce.place(x=50, y=110)
c = Button(window, text="C", font=("Nexa", 10), bd=2, height=1, width=4)
c.place(x=97, y=110)
plusminus = Button(window, text="+-", font=("Nexa", 10), bd=2, height=1, width=4)
plusminus.place(x=144, y=110)
sqrt = Button(window, text="√", font=("Nexa", 10), bd=2, height=1, width=4)
sqrt.place(x=191, y=110)

# third row (left to right)
seven = Button(window, text="7", font=("Nexa", 10), bd=2, height= 1, width=4)
seven.place(x=3, y=140)
eight = Button(window, text="8", font=("Nexa", 10), bd=2, height= 1, width=4)
eight.place(x=50, y=140)
nine = Button(window, text="9", font=("Nexa", 10), bd=2, height= 1, width=4)
nine.place(x=97, y=140)
divide = Button(window, text="/", font=("Nexa", 10), bd=2, height= 1, width=4)
divide.place(x=144, y=140)
modulus = Button(window, text="%", font=("Nexa", 10), bd=2, height= 1, width=4)
modulus.place(x=191, y=140)

# fourth row
four = Button(window, text="4", font=("Nexa", 10), bd=2, height= 1, width=4)
four.place(x=3, y=170)
five = Button(window, text="5", font=("Nexa", 10), bd=2, height= 1, width=4)
five.place(x=50, y=170)
six = Button(window, text="6", font=("Nexa", 10), bd=2, height= 1, width=4)
six.place(x=97, y=170)
multiply = Button(window, text="*", font=("Nexa", 10), bd=2, height= 1, width=4)
multiply.place(x=144, y=170)
reciprocal = Button(window, text="1/x", font=("Nexa", 10), bd=2, height= 1, width=4)
reciprocal.place(x=191, y=170)

# fifth row
one = Button(window, text="1", font=("Nexa", 10), bd=2, height= 1, width=4)
one.place(x=3, y=200)
two = Button(window, text="2", font=("Nexa", 10), bd=2, height= 1, width=4)
two.place(x=50, y=200)
three = Button(window, text="3", font=("Nexa", 10), bd=2, height= 1, width=4)
three.place(x=97, y=200)
minus = Button(window, text="-", font=("Nexa", 10), bd=2, height= 1, width=4)
minus.place(x=144, y=200)
equal = Button(window, text="=", font=("Nexa", 10), bd=2, height= 3, width=4, pady=-1)
equal.place(x=191, y=200)

# last row
zero = Button(window, text="0", font=("Nexa", 10), bd=2, height= 1, width=10, padx=-1)
zero.place(x=3, y=230)
decimal = Button(window, text=".", font=("Nexa", 10), bd=2, height= 1, width=4)
decimal.place(x=97, y=230)
plus = Button(window, text="+", font=("Nexa", 10), bd=2, height= 1, width=4)
plus.place(x=144, y=230)



window.mainloop()