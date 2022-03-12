from tkinter import *
from random import randint

root = Tk()
c = Canvas(root,width=500,height=500,bg="white")
c.pack()

ball=c.create_line(50,50,150,150)

root.mainloop()