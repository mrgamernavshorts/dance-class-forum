import tkinter
from tkinter import *
root = Tk()
def name():
    print(f"name :{user.get()}")
    print(f"class :{pas.get()}")

root.geometry("800x600")
root.minsize(800,600)
root.maxsize(800,600)

title = Label(text="DANCE CLASS FORUMS",font="arial 15 bold")
u = Label(text="name",font="arial 11 bold")
user = Entry(font="arial 10 bold")
p = Label(text="class",font="arial 11 bold")
pas = Entry(font="arial 10 bold")
b = Button(text="sumbit",command=name)

title.pack()
u.pack(pady="5px")
user.pack()
p.pack(pady="5px")
pas.pack()
b.pack(pady="5px")

root.mainloop()
