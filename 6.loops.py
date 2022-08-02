# *** Циклы ***

# Оператор while

# бесконечный цикл
# while True:
#   print("hello")

# цикл с условием
# val = 0

# while_val < 10:
#   print(f"Значение: {val}")
#    val = val + 1 = # длинный вариант
#    val +=1 = # короткий вариант


# val = 0






# прерывание цикла по дополнительному условию

# while True:
#    val = input("Enter the name: ")
#    if val == "stop":
#        print("Bye-bye!")
#        break
#    print(f"Hello, {val}!")

# val = 10
# while val > 0:
#    print(val)
#    val -= 1
#    if val < 5:
#       break


# пропуск части кода тела кода

# val = 0

# while val < 20:
    # 1 кусок кода
#    print(val)
#    val += 1

#    if val > 10:
#       continue


    # 2 кусок кода
    # print("Bye-bye!")
    # break
#    print(val + 100)

# val_0 = 0
# val_1 = 10

# while (val_0 < 10) and (val_1 > 0):
#     print(val_0, val_1)
#     val_0 += 1
#     val_1 -= 2



# Опреатор for

# 1. "читает" значение итерируемого обьекта(обьекта последовательности)
# 2. считанное значение присваиваются в собственную переменную
# 2. выполняет блок кода своего тела

# list_0 = (10, 20, 30, 40, 2, 5, 1, 879, 1800)

# for var in list_0:
#     var *= 10
#     print(var)

my_dict = {'a': 100, 'b': 200, 'c': 300}

# for item in my_dict.items():
#     print(item)

# for idx, val in my_dict.items():
#     print(idx, val)

# класс range()

r = range(10)
r = range(10, 20)
r = range(10, 100, 5)
r = range(-100, 100, 5)
 
t = tuple(r)

# print(t)

# for num in range(20):
#     print(num)

# безымянная переменная
for _ in range(5):
    print("hello")

