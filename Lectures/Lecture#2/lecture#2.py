# # lst = []
# # lst = list()
# # print(lst)
# lst = [1, 2, 3, 4]
# print(lst[0])

"""
Добавление эллемента в список
"""
# lst = [1, 5]
# print(lst)
# lst.append(8)
# print(lst)

# lst = []
# print(lst)
# for i in range(5):
#     lst.append(i)
#     print(lst)

"""
Удаление последнего эллемента
"""

# lst = [12, 7, -1, 21, 0]
# print(lst.pop())
# print(lst)
# print(lst.pop())
# print(lst)
# print(lst.pop())
# print(lst)

"""
Удаление конкретного эллемента списка
"""
# lst = [12, 7, -1, 21, 0]
# print(lst.pop(0))
# print(lst)

"""
Добавление Эллементов на нужную позицию
"""

# lst = [12, 7, -1, 21, 0]
# print(lst.insert(2, 11))
# print(lst)

"""
Срезы списков
"""

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(lst[0])
# print(lst[1])
# print(lst[len(lst)-1])
# print(lst[-5])
# print(lst[:])
# print(lst[:2])
# print(lst[len(lst)-2:])
# print(lst[2:9])
# print(lst[2:-18])
# print(lst[0: len(lst):6])
# print(lst[::6])
# print(type(lst))

"""
Кортежи - это неизменяеммый список
Кортеж занимает меньше места в памяти и работает быстрее, по сравнению со списком
"""

"""
Создание кортежа
"""
# #
# # t = ()
# # print(type(t))
# #
# # t = (1, 5 , 3)
# # print(type(t))
# #
# v = [1, 8 , 9]
# print(type(v))
# v = tuple(v)
# print(type(v))
#
# a,b,c = v
# print(a, b, c)

"""
Словари - это неупорядоченные коллекции произвольных объектов с доступом по ключу.
"""

d = {}
d = dict()

d['q'] = 'qwerty'
print(d)

d['w'] = 'werty'
print(d['q'])
