"""
Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!
Решите через рекурсию. В задании нельзя применять циклы.
"""

n = int(input("ВВедите число: "))


def proof(n):
    a = 0
    b = 0
    if n > a:
        b = b + n
        n -= 1
        print(a, b, n)
        proof(n)
    return b

proof(n)
print(b, n)
if b == (n * (n + 1) / 2):
    print("Выражение верно!")
else:
    print("Выражение неверно!")