# def sum(x, y):
#     return x + y

# def mylt(x, y):
#     return x * y

# def calc(op, a, b):
#     print(op(a, b))
# calc(mylt, 4, 5) # 20
# calc(sum, 4, 5) # 9

# def sum(x, y):
#     return x + y
# ⇔ (равносильно)
sum = lambda x, y: x + y


"""
В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
(число; квадрат числа).
Пример: 1 2 3 5 8 15 23 38
Получить: [(2, 4), (8, 64), (38, 1444)]
"""


# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = []

# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))
# print(res)

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = []

# def even_numbers_to (f, a):
#     return[f(i) for i in a]

# def even_numbers(f,a):
#     return[i for i in a if f(i)]

# res = even_numbers(lambda x: x % 2 == 0, data)
# print(res)

# res = even_numbers_to(lambda x : (x, x ** 2), res)
# print(res)


# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = []

# res = filter(lambda x: x % 2 == 0, data)
# print(res)

# res = map(lambda x : (x, x ** 2), res)
# print(res)

# res = list(filter(lambda x: x % 2 == 0, data))
# print(res)

# res = list(map(lambda x : (x, x ** 2), res))
# print(res)

#Функция zip () пробегает по минимальному входящему набору:

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]

#Функция enumerate() позволяет пронумеровать набор данных.

users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]

# list = ['yellow', 'blue', 'bus']
# main = open('File.txt', 'a') 
# main.writelines(list)
# main.close()

# with open('File.txt', 'w') as main:
#     main.write('Good job!\n')
#     main.write('Keep doing!\n')

# main = open('File.txt', 'r')
# for i in main:
#     print(i)
# main.close()

import os
print(os.getcwd())