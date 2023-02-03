"""
Напишите программу, которая принимает на вход координаты двух точек
и находит расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
"""

print('Введите через пробел координаты первой точки')
x1 , y1 = [float(i) for i in input().split()]
print('Введите через пробел координаты второй точки')
x2 , y2 = [float(i) for i in input().split()]
d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(round(d,3))