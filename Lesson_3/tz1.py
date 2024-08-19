# Задача 1
# n = int(input("Число: "))
# lst = []
# i = 1
# while i <= n:
#     lst.append(i)
#     i += 1
# print(lst)


# lst = []
# for i in range(1, 11):
#     lst.append(i)
# print(lst)

# Задача 2

# n = int(input("Число: "))
# i = 0
# lst = []
# while i < n:
#     lst.append(i)
#     i += 1
# print(lst)


# n = int(input("Число: "))
#
# for i in range(1, n):
#     print(i)


# Задача 3
# num = list(range(2, 21, 2))
# for i in num:
#     print(i)


# i = 2
# while i <= 20:
#      print(i)
#      i += 2


# Задача 4

# n = int(input("Число: "))
# i = 2
# while i <= n:
#      print(i)
#      i += 2


# n = int(input("Число: "))
# for i in range(0, n, 2):
#      print(i)


# Задача 5

# i = 0
# while i <= 9:
#      i += 1
#      print('1 *', i, '=', 1 * i)

# for i in range(1, 11):
#      print('1 *', i, '=', 1 * i)


# for i in range(1, 10):
#     for j in range(1, 10):   # вложенный цикл
#         print(i * j, end='\t')
#     print()

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i * j, end='\t')
#         j += 1
#     i += 1
#     print()


# Задача 6
# n = int(input("Число: "))

# for i in range(1, 11):
#     if n == i:
#         print(end='')
#     print(f"{n} * {i} = {i * n}")


# Задача 7
# n = int(input("Number: "))
# for i in range(n, 0, -1):
#     print(i)

# Задача 10
# word = input("Word: ")
# for i in word[::-1]:
#     print(i)

# Доп ЗАДачи
# arr = input('arr: ')
# counter = 0
# for word in arr.split():
#     if 'a' in word.lower():
#         counter += 1
#
# print(counter)
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# arr = "I'm Pyhton" # 1 2 3
# result = ''
# for letter in arr:
#     result += f"{alphabet.index(letter.lower()) + 1} "
# print(result)