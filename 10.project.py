 # Программа с графическим пользовательским интерфейсом

 # *** Генератор паролей ***

from cProfile import label
from curses import window
from distutils.cmd import Command
import hashlib as h
from tkinter import Tk, Label, Entry, Button, StringVar

def pwdGenerator(pwd_str) -> str:
    # кодирование в байт_строку
    byte_str = pwd_str.encode()
    # хеширование 
    hash_str = h.sha256(byte_str)
    # преобразование спец обьекта  хеш_строки в обычную строку
    hex_str = hash_str.hexdigest()[:10]
    # возврат хеш-строки
    return hex_str

# обьект окна
window = Tk()

# обьекты для хранения строк
raw_pwd = StringVar()
salt = StringVar()
hash_pwd = StringVar()
# виджет (компонент) текстовой метке
lbl = Label(text="password:")
lbl.grid(row=0, column=0)

# виджет поля ввода сырой пароли
Entry(textvariable=raw_pwd).grid(row=0, column=1)

# виджет текстовой метки
Label(text="Salt:").grid(row=1, column=0)

# виджет поля ввода "соли"
Entry(textvariable=salt).grid(row=1, column=1)

# виджет кнопки
def button_func():
    pwd = raw_pwd.get() + salt.get()
    hash_pwd.set(pwdGenerator(pwd))

Button(text="Пуск!", command=button_func).grid(row=2, column=0)

 # виджет поля вывода хеш-строки
Entry(textvariable=hash_pwd).grid(row=2, column=1)

# точка входа программы (место, где программа запускается)
window.mainloop()