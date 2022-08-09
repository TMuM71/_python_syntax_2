# *** Основы Обьектно-ориентированного программирования (ООП) ***

# Всё является обьектом
# Обьекты обладают свойствами (атрибутами) и методами (способности)
# Обьекты относятся к  определенным типам данных
# Класс - "чертёж" обьекта.
# Обьект = экземпляр (инстанс) класса.

# Создание (определения)

# Свойства

# 1 способ обьяления свойств

from cgitb import text


class Cat:
    # свойства (атрибуты)
    color = None
    name = None
    age = 2

# создание экземпляров (обьектов) класса Cat
cat_1 = Cat()
cat_2 = Cat()

# print(cat_1)

# запись значений в атрибуты
cat_1.name = "Мурка"
cat_1.color = "black"

cat_2.name = "Juchka"
cat_2.color = "green"
cat_2.age = 4

# чтение значений атрибутов
# print(cat_1.name, cat_1.color, cat_1.age)
# print(cat_2.name, cat_2.color, cat_2.age)

# 2 способ обьявления атрибутов

class Dog:
    # метод-конструктор (относится к " магическим" методам)
    def __init__(self, name_arg, age):
        self.name = name_arg
        self.age = age

# при обьявлении экземпляра класса можно передать параметры для атрибутов
dog_1 = Dog("Sharik", 5)

# print(dog_1.name, dog_1.age)

# метод 

class Cat_2:
    """"""
    Класс виртуального кота
    """"""
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age = age
    

    # метод (атрибут-метод) - функция, принадлежащая классу
    def mur(self):
        print("Mur-mur!")
    def info(self):
        text = f"Меня зовут {self.name}, мне {self.age} лет."
        print(text)

    def eat(self, food: str) -> str:
        return f"Я покушал {food}"
    
cat_1 = Cat_2("Barsik", 1)
cat_2 = Cat_2("Murka", 3)

# вызов методов
cat_1.mur()
cat_1.info()
print(cat_1.eat("бекон"))

cat_2.mur()
cat_2.info()
print(cat_2.eat("рыба"))

