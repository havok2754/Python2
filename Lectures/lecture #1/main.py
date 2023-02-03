# # a = 123
# # b = 1.23
# # print(a)
# # print(b)

# # a = "adfwe"
# # print(a)

# # print(type(a))

# a = 5
# b = 5.89
# c= 'hello'
# print(a, ' - ', b, ' - ', c)
# print(f"{a} - {b} - {c}")

# i  = 0
# while i < 5:
#     if i == 3:
#         break
#     i = i + 1
# else:
#     print("Пожалуй")
#     print('хватит )')
# print(i)

n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0:
        flag = False
        print(i)
    elif i > n // 2:
        print(n)
        flag = False
    i += 1