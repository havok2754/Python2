"""
Напишите программу для. проверки истинности утверждения
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
для всех значений предикат.
"""

from random import randint

x = randint(0, 1)
y = randint(0, 1)
z = randint(0, 1)

print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z}')
if not (x or y or z) == (not x and not y and not z):
    print('Выражение верно!')
else:
    print('Выражение неверно!')