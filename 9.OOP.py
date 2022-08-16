# Принципы ООП

# Принцип Наследования

# родительский (предковый) класс 
from base64 import b16decode, b32decode, b32hexdecode
from tokenize import String
from unicodedata import name
from xml.dom.minidom import Attr


class Animal:
    def __init__(self, num_legs):
        self.num_legs = num_legs

    def move(self):
        print("Я двигаюсь")

    def get_num_legs(self):
        print(f"У меня {self.num_legs} ноги")

# дочерние классы
class Mammal(Animal):
    def __init__(self, num_legs, name):
        super().__init__(num_legs)    
        self.name = name
    
    def info(self):
        print(f"Меня зовут {self.name}")
        self.get_num_legs()

class Insect(Animal):
    def info(self):
        print("Жуу-жуу!")
        self.get_num_legs()

human_1 = Mammal(2, "John")

bug_1 = Insect(6)


# human_1.move()
# human_1.info()

# bug_1.move()
# bug_1.info()

# Принцип Полиморфизма

# Полиморфизм операторов
res = 2 + 3 # арифметическое сложение
res = '2' + '3' # конкатенация

# Полиморфизм с "магическими" (методами перегрузки операторов)
class Computer_1:
    def my_sum(self, a, b):
        print(a + b)

comp_1 = Computer_1()
# comp_1.my_sum(2, 5)
# comp_1(2, 5)

class Computer_2:
    def __call__(self, a, b):
        print(a + b)

comp_2 =Computer_2()
# comp_2(2, 5)

# Полиморфизм методов
class A:
    def m_1(self, arg):
        print(arg, + 10)

class B:
    def m_1(self, arg):
        print(arg ** 2)

a = A()
b = B()

# a.m_1(10)
# b.m_1(10)

# Принцип Инкапсуляции

# без инкапсуляции
class x1:
    attr_1 = 100

    def m_1(self):
        print(f"Attribute value: {self.attr_1}")

obj_x1 = x1()

# print(obj_x1.attr_1)
# obj_x1.m_1()

# не строгая инкапсуляция
class x2:
    _attr_1 = 200

    def _m_1(self):
        print(f"Attribute value: {self._attr_1}")

obj_x2 = x2()

# print(obj_x2._attr_1)
# obj_x2._m_1()

# строгая инкапсуляция
class x3:
    __attr_1 = 300

    def __m_1(self):
        print(f"Attribute value: {self.__attr_1}")

obj_x3 = x3()

# print(obj_x3.__attr_1)
# obj_x3.__m_1()

# лазейка
# print(obj_x3._x3__attr_1)
# obj_x3._x3__m_1()

# Принцип Композиции (Агрегации)

class Library("var books"):
    print()

class Book():
    let_name: String
    init = ("name: String, self.name = name")

let_lib = Library()

let_b1 = Book, name b1("-> Введение в программирование")

let_b2 = Book, name b2("-> Вперёд к программированию!")

let_b3 = Book, name b3("-> Программирование")

