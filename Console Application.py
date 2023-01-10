import numpy as np
import matplotlib.pyplot as plt
import math


def f(x):
    return x ** 3 - 5.9 * x ** 2 + 11.1 * x - 6.7  # задаем функцию по варианту


def halfDivision(a, b, epsilon):   # метод половинного деления
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
    print("Корень:", c)
    print("Невязка:", "{:e}".format(-f(c)))
    print("Число итераций:", n)
    return c


def secantMethod(epsilon):             # метод секущих
    m = 0
    print("Начальное приближение:  x0: ")
    x0 = float(input())
    print("Начальное приближение:  x1: ")
    x1 = float(input())
    while math.fabs(x1 - x0) > epsilon:
        xk = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0 = x1
        x1 = xk
        m += 1
    print("Корень:", x1)
    print("Невязка:", "{:e}".format(-f(x1)))
    print("Число итераций:", m)


def plot_graph():           # функция построения графика функции
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


def main():
    plot_graph()
    print("Введите epsilon = ")
    epsilon = float(input())
    flag = True
    while flag:
        n = 0
        a = float(input("Введите левую границу интервала: "))
        b = float(input("Введите правую границу интервала: "))
        print("Результат метода половинного деления")
        halfDivision(a, b, epsilon)
        print("Результат метода секущих")
        secantMethod(epsilon)
        ans_flag = True
        while ans_flag:
            ans = input("Хотите найти ещё один корень? (да/нет): ")
            if ans == 'нет' or ans == 'да':
                ans_flag = False
                if ans == 'нет':
                    flag = False
            else:
                print("Введите только да или нет.")


if __name__ == '__main__':
    main()

