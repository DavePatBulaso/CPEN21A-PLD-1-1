from tkinter import *
window = Tk()

# add widgets from here
window.geometry("240x260+760+400")
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
seven = Button(window, text="8", font=("Nexa", 10), bd=2, height= 1, width=4)
seven.place(x=50, y=140)
seven = Button(window, text="9", font=("Nexa", 10), bd=2, height= 1, width=4)
seven.place(x=97, y=140)
seven = Button(window, text="/", font=("Nexa", 10), bd=2, height= 1, width=4)
seven.place(x=144, y=140)
seven = Button(window, text="%", font=("Nexa", 10), bd=2, height= 1, width=4)
seven.place(x=191, y=140)

# fourth row
seven = Button(window, text="4", font=("Nexa", 10), bd=2, height= 1, width=4)
seven.place(x=3, y=170)
seven = Button(window, text="5", font=("Nexa", 10), bd=2, height= 1, width=4)
seven.place(x=50, y=170)
seven = Button(window, text="6", font=("Nexa", 10), bd=2, height= 1, width=4)
seven.place(x=97, y=170)
seven = Button(window, text="*", font=("Nexa", 10), bd=2, height= 1, width=4)
seven.place(x=144, y=170)
seven = Button(window, text="1/x", font=("Nexa", 10), bd=2, height= 1, width=4)
seven.place(x=191, y=170)

# fifth row
one = Button(window, text="1", font=("Nexa", 10), bd=2, height= 1, width=4)
one.place(x=3, y=200)
one = Button(window, text="2", font=("Nexa", 10), bd=2, height= 1, width=4)
one.place(x=50, y=200)
one = Button(window, text="3", font=("Nexa", 10), bd=2, height= 1, width=4)
one.place(x=97, y=200)
one = Button(window, text="-", font=("Nexa", 10), bd=2, height= 1, width=4)
one.place(x=144, y=200)
one = Button(window, text="=", font=("Nexa", 10), bd=2, height= 3, width=4, pady=-1)
one.place(x=191, y=200)

# last row
one = Button(window, text="0", font=("Nexa", 10), bd=2, height= 1, width=10, padx=-1)
one.place(x=3, y=230)
one = Button(window, text=".", font=("Nexa", 10), bd=2, height= 1, width=4)
one.place(x=97, y=230)
one = Button(window, text="+", font=("Nexa", 10), bd=2, height= 1, width=4)
one.place(x=144, y=230)



window.mainloop()