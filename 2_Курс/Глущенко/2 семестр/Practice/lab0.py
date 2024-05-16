from tkinter import *
import math

route_flag=True

def motion():
    small_oval[4] += small_oval[5] #новое расстояние до следующей точки (скорость движения)
    canv.coords(small_oval_for_drow, calculate_coord(small_oval))
    root.after(20, motion)

def route():
    global route_flag
    if route_flag == False:
        small_oval[5] = small_oval[5] * (-1)
        route_flag=True
def route_left():
    global route_flag
    if route_flag == True:
        small_oval[5] = small_oval[5] * (-1)
        print("change left")
        route_flag = False


def new_speed(root):
    small_oval[5] = (small_oval[5] / abs(small_oval[5])) * scale1.get()
    print(scale1.get())


def calculate_coord(coords):
    middle_x, middle_y, radius, distance, angle, sp = coords
    x = middle_x - distance * math.sin(math.radians(-angle))
    y = middle_y - distance * math.cos(math.radians(-angle))
    x_first = x - radius
    y_first = y - radius
    x_new = x + radius
    y_new = y + radius
    return x_first, y_first, x_new, y_new


big_oval = [300, 300, 200, 0, 0, 0]  #  набор данных для большого круга (координы x и y центра, радиус, угол и угловая скорость
small_oval = [300, 300, 10, 200, 0, 5]  #  набор данных для маленького круга (координы x и y центра, радиус маленького и большого круга, скорость движения по оси

root = Tk()
canv = Canvas(root, width=600, heigh=600, bg="lightblue")

scale1 = Scale(root,orient=HORIZONTAL,length=200,from_=1,to=15,resolution=1)
Button(root,text=u"Нажмите для выхода", command=root.destroy).pack()
Button(root,text=u"Нажмите для движения по часовой стрелка", command=route).pack()
Button(root,text=u"Нажмите для движения против часовой стрелка", command=route_left).pack()
scale1.pack()
scale1.bind("<Motion>",new_speed)
canv.create_oval(calculate_coord(big_oval))
small_oval_for_drow = canv.create_oval(calculate_coord(small_oval), fill="green")

canv.pack()
motion()  #Запуск анимации движения маленького круга по оси большого
root.mainloop()