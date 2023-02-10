"""
Реализуйте алгоритм перемешивания списка.
"""

import random

print('Введите список через пробел')
page = list(map(str, input().split()))
random.shuffle(page)
print(page)