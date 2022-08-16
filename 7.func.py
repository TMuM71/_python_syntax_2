# *** Функции ***

# 1 вариант
# Функция, которая не принимает параметры (данные) (нет аргументов) и ничего не возвращает

# Определение (создание) функции
from cgitb import reset


def func_1():
    """
    Наша первая функция
    """
    v_0 = 100
    v_1 = 200
    res = v_0 + v_1
    print(res)
    
# вызов функции
# func_1()

# 2 вариант 
# Функция, которая принимает параметры (обладает аргументами) и ничего не возвращает

def func_2(arg_0):
    res = arg_0 ** 2
    print(res)

# func_2(100)

def func_3(a_1, a_2, a_3):
    res = a_1 * a_2 + a_3 * 2
    print(res)

# func_3(5, 2, 2)


# аргументы с значениями по умолчанию
def func_4(a=5, b=0):
    c = a + b
    print(c)

# func_4()

# # позиционная передача параметров
# func_4(10)
# func_4(10, 20)

# # именованная пеоедача параметров
# func_4(b=20, a=10)

def func_5(a, b=10, c=20):
    print(a + b + c)

# func_5(100, c=10)

# передача произвольного кол-ва позиционных параметров
def func_6(*args):
    print(args)
    
    if len(args) > 1:
        res = args[0] + args[1]
    else:
        res = args[0] + 10
    print(res)

    s = 0
    for num in args:
        s += num
    print(s)

# func_6(10)
# func_6(10, 5, 2, 5, 5)

# передача произвольного кол-ва именованных параметров
def func_7(**kwargs):
    print(kwargs)

    res = kwargs["arg_1"] + kwargs['b']
    print(res)
# func_7(arg_1=10, b=20, name="python")

# 3 вариант
# Функция, которая возвращает значения

def func_8(a, b):
    res = a ** b
    return res

var_1 = func_8(10, 3)

def func_9(a, b, c):
    res_0 = a * b
    res_1 = b + c
    return res_0, res_1

# var_1 = func_9(2, 3, 4)

# var_1, var_2 = func_9(2, 3. 4)
# print(var_1)
# print(var_2)


# пример. Функция, вычисляющая Евклидово расстояние

import math

def euklid(coord_1, coord_2):
    q_katet_x = (coord_1[0] - coord_2[0]) ** 2
    q_katet_y = (coord_1[1] - coord_2[1]) ** 2

    gipot = math.sqrt(q_katet_x + q_katet_y)

    return gipot

a = (10, 20)
b = (-5, 15)

s = euklid(a, b)

# print(s)
 
# Лямда-выражение (лямда-функция, безымянная функция)

my_lambda = lambda a, b: a * b

res = my_lambda(5, 3)

# print(res)

def func_10(f, a, b):
    res = f(a, b)
    print(res)

func_10(lambda x, y: x ** y, 10, 3)