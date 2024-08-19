# List comprehensions

# Задача 1
# a = int(input("Num: "))
# b = int(input("Num: "))
# num = [n*n for n in range(a, b)]
# print(num)

# Задача 2
# a = int(input("Num: "))
# b = int(input("Num: "))
# num_even = [n for n in range(a, b,) if n % 2 == 0]
# print(num_even)

# Задача 3
# array = input("word: ")
# vowels = ('а', 'о', 'у', 'и', 'ы', 'э')
# world = [n for n in array.lower() if n in vowels]
# print(world)

# Задача 4
# arr = [n for n in range(1, 101) if n % 3 == 0 and n % 5 == 0]
# print(arr)

# Задача 5
# lists = [[i, i + 1, i + 2, i + 3] for i in range(1, 10, 4)]
# print(lists)


# Задача 1

# n = input("String: ")
# l = [ord(i) for i in n]
# print(l)

# Задача 2
# user = input("Num: ")
# num = [n for n in max(user)]
# print(num)

# ЗАдача 3
# str = "is2 Thi1s T4est 3a"
# res = [n for n in str.split()]
# lst = res
# print(f"{lst[0]} {lst[1]} {lst[2]} {lst[3]} = {lst[1]} {lst[0]} {lst[3]} {lst[2]}")

# array = 'is2 Thi1s T4est 3a'.split()
# res = dict()
#
# for word in array:
#     for symbol in word:
#         if symbol.isdigit():
#             res[int(symbol)] = word
# new_res = sorted(res.items())
# array = " "
# print(new_res)
# for item in new_res:
#     array += f"{item[-1]} "
# print(array)

# Задача 4
# a = [
#     {'name': "Walter", "age": 52, "marks": [4, 5, 4, 5, 5]},
#     {'name': "Anatoli", "age": 35, "marks": [4, 5, 4, 5, 5]},
#     {'name': "Gustavo", "age": 17, "marks": [4, 5, 4, 5, 5]},
#     {'name': "Mike", "age": 25, "marks": [4, 5, 4, 5, 5]},
# ]
#
# for i in range(len(a) - 1):
#     for j in range(len(a) - 1 - i):
#         if a[j]['age'] < a[j + 1]['age']:
#             a[j], a[j + 1] = a[j + 1], a[j]
#
#
# Задача 5
# r = int(input("Num: "))
#
# lst = [u for u in range(r)]
# l_one = [n ** 2 for n in lst]
# l_two = [i / 2 for i in lst[1:11]]
# l_three = [i for i in lst if i % 2 == 0]
# l_for = [i for i in lst if i % 2 != 0]
# l_five = [i for i in lst if i % 3 != 0]
# print(l_one)