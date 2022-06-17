#cd "/home/glushchenko/git/FA/2 Курс/Глущенко/2 семестр/Practice"
from tkinter import *
from tkinter import ttk
from math import sin, cos, pi
root = Tk()
frm = ttk.Frame(root, padding=10)

root.title("Глущенко Суперэллипс")
ttk.Label(frm, text="Hello World!",anchor="center").pack()


def sgn(x):
    return ((x > 0) - (x < 0)) * 1 # функция из обощения


canv = Canvas(root, width = 1000, height = 1000, bg = "lightblue", cursor = "pencil")
#canv.create_line(500,1000,500,0,width=2,arrow=LAST)
#canv.create_line(0,500,1000,500,width=2,arrow=LAST)


def getV(root):

    canv.create_rectangle(290,290,710,710,fill="lightblue",outline="lightblue")
    n = scale1.get()
    label = Label(font='sans 20')
    label.pack()
    label.after(1,tick(n))



scale1 = Scale(root,orient=HORIZONTAL,length=200,from_=0.1,to=3,resolution=0.1)
Button(root,text=u"Нажмите для выхода", command=root.destroy).pack()
Label(text="Для отрисовки суперэллипса передвигайте ползунок (это изменяет значение n)").pack()
scale1.pack()
scale1.bind("<Motion>",getV)


def tick(n):
    a, b = 200, 200  # начальные значения
    na = 2 / n
    step = 10000  # шаг для отрисовки
    piece = (pi * 2) / step
    t = 0
    for t1 in range(16000):
        # так записано, потому что sin^n(x) равонзначно (sin(x))^n
        x = 500 + (abs((cos(t))) ** na) * a * sgn(cos(t))
        y = 500 + (abs((sin(t))) ** na) * b * sgn(sin(t))
        t += piece
        canv.create_oval(x, y, x + 1, y + 1, fill='black')

    #canv1 = Canvas(root, width=1000, height=1000, bg="lightblue", cursor="pencil")
    #canv1.pack()


canv.pack()


root.mainloop()