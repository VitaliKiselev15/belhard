# 3,4 домашнее задание
# Создать программу, которая на вход получает данные о треугольниках (а именно катеты) Выводит на экран информацию о каждом треугольнике в формате:
# Треугольник 1 с катетами {a} и {b} имеет площадь {S} и гипотенузу {c}
# TODO: Ввод нескольких треугольников -> зациклить, или бесконечный цикл пока не завершиться программа

import string

#  функцию ввода числа
def input_number(strint_output):
    number = 0
    # бесконечный цикл до возникновения исключения
    while True:        
        try:
            number = int(input(strint_output))

        # проверяем число
        except ValueError:
            # цикл до правильного ввода
            print("NonNumericError! It's not a number, try again.")

        # выходим из цикла если введено число
        else:
            print("OK")
            break
    return number

# функция разбора входной строки 
def get_num_string(input_string):
    get_a=get_b=0
    # разбиваем строку на два числа.
    # числа между собой могут разделяться ","," " остальное не реагируем
    # берем только первые два числа остальное пропускаем

    # если разделитель пробел
    pos = input_string.find(" ")    
    if pos == -1:
        # если разделитель ","
        pos = input_string.find(",")
        if pos!=-1:
            input_string.split(",")
    else:
        input_string.split()

    if pos !=-1:
        try:
            get_a = int(input_string.split(",")[0])
            get_b = int(input_string.split(",")[1])
        # проверяем число
        except ValueError:
             print("NonNumericError! It's not a number, try again.")

    else:
        print("Separator not supported")

    return get_a,get_b

# 1. ввод через отдельну строку, преобразования в числа. запрашиваем два катета
#a = input_number("Input A:")
#b = input_number("Input B:")

# 2. запрашиваем два числа одной строкой
input_str = input("Input A and B:")
a,b = get_num_string(input_str)

# ни один из катетов не должен быть равен нулю
if a == 0 or b == 0:
    print ("numbers can't be zero")
else:
    s = (a*b)/2 # площать треугольника
    g = (a**2+b**2)**0.5 # гипотенуза
    
    print("For a =",a,"and b =",b," square =",s, " hypotenuse=",g)
