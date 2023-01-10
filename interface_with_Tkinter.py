from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.messagebox import showerror
import warnings
import math


def evaluate(event):        # функция построения графика в главном окне
    try:
        mystr = entry.get()
        exec('f = lambda x:' + mystr, globals())
        a = float(strA.get())
        b = float(strB.get())
        X = np.linspace(a, b, 10000000)
        Y = [f(x) for x in X]
        ax.clear()
        ax.plot(X, Y, color="darkmagenta", label="y(x)", linewidth=2)
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.legend()
        ax.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
        canvasAgg.draw()  # перерисовать "составной" холст
        return
    except:  # реакция на любую ошибку
        showerror('Ошибка', "Неверное выражение или интервал [a,b].")


def evaluate2(event):  # функция обработки ошибки, чтобы кнопка отжималась при ошибке
    window.after(100, evaluate, event)


def halfDivision():   # метод половинного деления
    a = EntryA.get()
    a = float(a)
    b = EntryB.get()
    b = float(b)
    epsilon = EntryEPS1.get()
    epsilon = float(epsilon)
    c = (a + b) / 2
    n = 0
    while (b - a) >= 2 * epsilon:
        n += 1
        if f(c) == 0:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2
    str1 = str(c)
    res1 = 'Корень: ' + str1
    str2 = str("{:e}".format(-f(c)))
    res2 = '\nНевязка: ' + str2
    str3 = str(n)
    res3 = '\nЧисло итераций: ' + str3
    ResultText1.delete(1.0, END)
    ResultText1.delete(2.0, END)
    ResultText1.delete(3.0, END)
    ResultText1.insert(1.0, res1)
    ResultText1.insert(2.0, res2)
    ResultText1.insert(3.0, res3)


def plot_graph():               # функция построения графика
    x = np.linspace(1, 3, 10000000)
    fig, ax = plt.subplots()
    ax.plot(x, f(x), color="blue", label="y(x)")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    fig.set_figwidth(8)
    fig.set_figheight(6)
    plt.grid()
    plt.show()


def clear1():                   # функция очистки поля для результатов метода половинного деления
    ResultText1.delete(1.0, END)
    ResultText1.delete(2.0, END)
    ResultText1.delete(3.0, END)


def secantMethod():             # метод секущих
    m = 0
    x0 = EntryX0.get()
    x0 = float(x0)
    x1 = EntryX1.get()
    x1 = float(x1)
    epsilon = EntryEPS2.get()
    epsilon = float(epsilon)
    while math.fabs(x1 - x0) > epsilon:
        xk = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0 = x1
        x1 = xk
        m += 1
    str1 = str(x1)
    res1 = 'Корень: ' + str1
    str2 = str("{:e}".format(-f(x1)))
    res2 = '\nНевязка: ' + str2
    str3 = str(m)
    res3 = '\nЧисло итераций: ' + str3
    ResultText2.delete(1.0, END)
    ResultText2.delete(2.0, END)
    ResultText2.delete(3.0, END)
    ResultText2.insert(1.0, res1)
    ResultText2.insert(2.0, res2)
    ResultText2.insert(3.0, res3)


def clear2():                       # функция очистки поля для результатов метода секущих
    ResultText2.delete(1.0, END)
    ResultText2.delete(2.0, END)
    ResultText2.delete(3.0, END)


window = Tk()
window.geometry('1000x1000')
window.title("Методы решения нелинейных скалярных уравнений")
warnings.filterwarnings("error")
frameUp = Frame(window, relief=GROOVE, height=150)
frameUp.pack(side=TOP, fill=X)
Label(frameUp, text="Введите исследуемую функцию:").place(x=2, y=4, width=200, height=25)
Label(frameUp, text="Начало интервала a:").place(x=260, y=4, width=140, height=25)
Label(frameUp, text="Конец интервала b:").place(x=420, y=4, width=140, height=25)
# str = StringVar()
# str.set('x ** 3 - 5.9 * x ** 2 + 11.1 * x - 6.7')
entry = Entry(frameUp, relief=RIDGE, borderwidth=4)
entry.bind("<Return>", evaluate)
entry.place(x=6, y=30, width=250, height=25)
strA = StringVar()
strA.set(1)
entryA = Entry(frameUp, relief=RIDGE, borderwidth=4, textvariable=strA)
entryA.place(x=280, y=30, width=80, height=25)
entryA.bind("<Return>", evaluate)
strB = StringVar()
strB.set(3)
entryB = Entry(frameUp, relief=RIDGE, borderwidth=4, textvariable=strB)
entryB.place(x=450, y=30, width=80, height=25)
entryB.bind("<Return>", evaluate)

fig = Figure(figsize=(7, 5), facecolor='white')
ax = fig.add_subplot(111)
canvasAgg = FigureCanvasTkAgg(fig, master=window)
canvasAgg.draw()
canvas = canvasAgg.get_tk_widget()
canvas.pack(expand=False, anchor=N)
btn = Button(window, text='Построить график')
btn.bind("<Button-1>", evaluate2)
btn.pack(ipady=2, pady=4, padx=10)
#
frameBottom = Frame(window, relief=SUNKEN, height=150)
frameBottom.pack(side="bottom", fill=Y)

Label(window, text="Методы решения: ").place(x=300, y=690, width=100, height=25)
Label(window, text="Метод половинного деления:").place(x=50, y=720, width=200, height=25)
Label(window, text="a").place(x=50, y=745, width=50, height=20)
Label(window, text="b").place(x=50, y=775, width=50, height=20)
Label(window, text="epsilon").place(x=50, y=810, width=50, height=20)
EntryA = Entry(window, width=10, font='Arial 14')
EntryA.place(x=90, y=740, width=140, height=25)
EntryB = Entry(window, width=10, font='Arial 14')
EntryB.place(x=90, y=770, width=140, height=25)
EntryEPS1 = Entry(window, width=10, font='Arial 14')
EntryEPS1.place(x=100, y=805, width=135, height=25)
ResultText1 = Text(width=30, height=4)
calcBut1 = Button(window, text='Вычислить', command=halfDivision)
calcBut1.place(x=100, y=840, width=100, height=25)
calcBut2 = Button(window, text='Очистить', command=clear1)
calcBut2.place(x=220, y=840, width=100, height=25)
ResultText1.place(x=90, y=870)


Label(window, text="Метод секущих:").place(x=600, y=720, width=140, height=25)
Label(window, text="Начальное приближение:  x0: ").place(x=450, y=745, width=200, height=20)
Label(window, text="Начальное приближение:  x1: ").place(x=450, y=775, width=200, height=20)
Label(window, text="epsilon").place(x=600, y=810, width=50, height=20)
EntryX0 = Entry(window, width=10, font='Arial 14')
EntryX0.place(x=640, y=740, width=140, height=25)
EntryX1 = Entry(window, width=10, font='Arial 14')
EntryX1.place(x=640, y=770, width=140, height=25)
EntryEPS2 = Entry(window, width=10, font='Arial 14')
EntryEPS2.place(x=650, y=805, width=135, height=25)
ResultText2 = Text(width=30, height=4)
calcBut3 = Button(window, text='Вычислить', command=secantMethod)
calcBut3.place(x=610, y=850, width=100, height=25)
calcBut4 = Button(window, text='Очистить', command=clear2)
calcBut4.place(x=730, y=850, width=100, height=25)
ResultText2.place(x=600, y=880)

window.bind('<Control-z>', lambda event: window.destroy())
window.mainloop()
