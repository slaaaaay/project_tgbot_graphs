'''в этом файле прописаны функции для работы с уравнениями функций'''
import matplotlib.pyplot as plt
from aiogram.types import FSInputFile
def f_graph_root(a, b, c):
    '''функция рисует график функции корня х и сохраняет его в переменной photo в формате png'''
    plt.clf()
    # очищает график, если бот уже использовался
    list_x = list()
    list_y = list()
    for x in range(-50, 50):
        y = (a*x+b)**0.5 + c
        list_x.append(x)
        list_y.append(y)
    plt.plot(list_x, list_y)
    # строит график
    plt.grid()
    # чертит сетку

    arrowprops = {'arrowstyle': '->'}
    plt.annotate('', xy=(50, 0), xytext=(-50, 0), arrowprops=arrowprops)
    plt.annotate('', xy=(0, 50), xytext=(0, -50), arrowprops=arrowprops)
    # созадет стрелочки для Ох и Оу
    plt.savefig('image.png')
    photo = FSInputFile('image.png')
    return photo

def f_graph_gip(k, a):
    '''функция рисует график гиперболы и сохраняет его в переменной photo в формате png'''
    plt.clf()
    list_x = list()
    list_y = list()
    for x in range(-50, 50):
        if x + a != 0:
            y = k / (x + a)
            list_x.append(x)
            list_y.append(y)

    plt.plot(list_x, list_y)
    plt.grid()

    arrowprops = {'arrowstyle': '->'}
    plt.annotate('', xy=(50, 0), xytext=(-50, 0), arrowprops=arrowprops)
    plt.annotate('', xy=(0, 50), xytext=(0, -50), arrowprops=arrowprops)

    plt.savefig('image.png')
    photo = FSInputFile('image.png')
    return photo

def f_graph_cube(a, b):
    '''функция рисует график кубической функции и сохраняет его в переменной photo в формате png'''
    plt.clf()
    list_x = list()
    list_y = list()
    for x in range(-50, 50):
        y = a*x**3 + b
        list_x.append(x)
        list_y.append(y)
    plt.plot(list_x, list_y)
    plt.grid()

    arrowprops = {'arrowstyle': '->'}
    plt.annotate('', xy=(50, 0), xytext=(-50, 0), arrowprops=arrowprops)
    plt.annotate('', xy=(0, 50), xytext=(0, -50), arrowprops=arrowprops)

    plt.savefig('image.png')
    photo = FSInputFile('image.png')
    return photo

def f_graph_square(a, b, c):
    '''функция рисует график квадратичной функции и сохраняет его в переменной photo в формате png'''
    plt.clf()
    list_x = list()
    list_y = list()
    for x in range(-50, 50):
        y = a*x**2 + b*x + c
        list_x.append(x)
        list_y.append(y)
    plt.plot(list_x, list_y)
    plt.grid()

    arrowprops = {'arrowstyle': '->'}
    plt.annotate('', xy=(50, 0), xytext=(-50, 0), arrowprops=arrowprops)
    plt.annotate('', xy=(0, 50), xytext=(0, -50), arrowprops=arrowprops)

    plt.savefig('image.png')
    photo = FSInputFile('image.png')
    return photo

def f_graph_line(k, b):
    '''функция рисует график линейной функции и сохраняет его в переменной photo в формате png'''
    plt.clf()
    list_x = list()
    list_y = list()
    for x in range(-50, 50):
        y = k*x + b
        list_x.append(x)
        list_y.append(y)
    plt.plot(list_x, list_y)
    plt.grid()

    arrowprops = {'arrowstyle': '->'}
    plt.annotate('', xy=(50, 0), xytext=(-50, 0), arrowprops=arrowprops)
    plt.annotate('', xy=(0, 50), xytext=(0, -50), arrowprops=arrowprops)

    plt.savefig('image.png')
    photo = FSInputFile('image.png')
    return photo

def graph(equation):
    '''функция рисует график записанного уравнения и сохраняет его в переменной photo в формате png'''
    plt.clf()
    list_x = list()
    list_y = list()
    for x in range(-50, 50):
        for y in range(-50, 50):
            if eval(equation):
                list_x.append(x)
                list_y.append(y)
                # при верном равенстве введенного уравнения элементы добавляются в список

    plt.plot(list_x, list_y)
    plt.grid()
    arrowprops = {'arrowstyle': '->'}
    plt.annotate('', xy=(50, 0), xytext=(-50, 0), arrowprops=arrowprops)
    plt.annotate('', xy=(0, 50), xytext=(0, -50), arrowprops=arrowprops)

    plt.savefig('image.png')
    photo = FSInputFile('image.png')
    return photo


