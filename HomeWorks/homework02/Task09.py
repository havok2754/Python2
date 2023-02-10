"""
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt в одной строке одно число.
"""

with open ('file.txt', 'r') as f:
    positions = f.read().split('\n')
positions = list(map(int, positions))

N = int(input("Введите число: "))
spam = list(range(-N, N+1))
print(spam)
prod = 1
for x in positions:
    i = int(x)
    prod = prod * spam[i]
print(prod)