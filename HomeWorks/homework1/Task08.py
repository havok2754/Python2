"""
Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y).
"""
print('Введите номер четверти')
a = int(input())

if a == 1:
    print('Диапозон возможных координат точки -  Х > 0, Y > 0')
elif a == 2:
    print('Диапозон возможных координат точки -  Х < 0, Y > 0')
elif a == 3:
    print('Диапозон возможных координат точки -  Х < 0, Y < 0')
elif a == 4:
    print('Диапозон возможных координат точки -  Х > 0, Y < 0')
else:
    print('Неверное число')