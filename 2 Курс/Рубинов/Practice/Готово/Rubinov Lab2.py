from tkinter import *
from random import *


root = Tk()
root.title("Рубинов Дождь")
c = Canvas(width=800, height=600,
           bg='lavender')
c.focus_set()
c.pack()
t = 0

# Движение
def motion():
    c.move('rain',0,15)
    c.move('rain2', 0, 10)
    c.move('rain3', 0, 5)


# Поевление капель
while t < 5000:
    x0 = randint(0, 800)
    y0 = randint(0, 600)
    x1 = randint(0, 800)
    y1 = randint(0, 600)
    x2 = randint(0, 800)
    y2 = randint(0, 600)
    drop = c.create_rectangle(x0,y0,x0 + 5,y0 + 30, fill='violet', tag='rain', outline="")
    drop2 = c.create_rectangle(x1, y1, x1 + 5, y1 + 20, fill='plum', tag='rain2', outline="")
    drop3 = c.create_rectangle(x2, y2, x2 + 5, y2 + 10, fill='thistle', tag='rain3', outline="")
    motion()
    root.update()
    t += 1

root.mainloop()