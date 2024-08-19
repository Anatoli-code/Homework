# Задача 1

# def world(a, b, c):
#     x = a ** 2, b ** 2, c ** 2
#     return list(x)
# print(world(5, 5, 5))

# Задача 2

# def func(letters: str) -> str:
#     return [i for i in letters.split() if len(i) > 5]
#
# s = "Привет, я живу в Пинске"
# print(func(s))

# Задача 3

# def num(x):
#     return [i for i in x if i % 2 == 0]
# print(num(range(1, 51)))

# ЗАдача 4

# def num(x):
#     return [i*i for i in x if i % 2 == 0]
#
# print(num(range(1, 51)))

# Задача 5

# def world(x):
#     letter = 'а'
#     return [i for i in list_a if i[0].lower() == letter]
#
# list_a = ['Анатолий', 'Пинск', 'Адреналин', 'Толик']
# print(world(list_a))

# Задача 6

# def num(x):
#     return [i for i in x if i > 10 and i < 20]
#
# print(num(range(1,30)))

# Задача 7

# def world(x):
#     letter = 'е'
#     return [i for i in list_a if letter.lower() in i]
# list_a = ['Вероника', 'Анатолий', 'Екатеринбург', 'Александр']
# print(world(list_a))


# Задача 8

# def num(x):
#     for i in x:
#         for j in x:
#             if j < 0:
#                 return False
#
#         return True
#
# list_a = [1, 2, -3, 4, 5, 6, 7, 8, 9, 10]
# print(num(list_a))



# ЗАдача 9
# def pit(f):
#     integ= []
#     for i in f:
#         if type(i) != str:
#             integ.append(i)
#     return integ
#
# lst = ['strs', 25, 23, 20, 'saw']
# print(pit(lst))

# def pit(x):
#     return [num for num in x if num.isdigit()]
# lst = ["The", 'test', "str444ing", 'Hello12', '1233212']
# print(pit(lst))

# Задача 10

# def sqr(x):s
#     i = 1
#     while i < x:
#         yield i
#         i = i*2
#
# for i in sqr(x=1000):
#     print(i)

# Доп Задачи

# def get_digit_square_sum(number: int) -> int:
#     digits = list(str(number))
#     result = [int(i) ** 2 for i in digits]
#     return sum(result)
#
# print(get_digit_square_sum(312))



# def even_or_odd(num: int) -> bool:
#     if num % 2 == 0:
#         return True
#     return False
#
# print(sorted([1, 2, 3, 4, 5, 6, 7, 8], key=even_or_odd))


# def get_common_elems(lst_1, lst_2):
#     return [i for i in lst_1 if i in lst_2]
#
# print(get_common_elems([1, 2, 3], [1, 2, 6]))


#-----------------------------------------------------------
def mult(array: list) -> int:
    result = array[0]
    for i in array[1:]:
        result *= i
    return result

def div(array: list) -> int:
    result = array[0]
    for i in array[1:]:
        result /= i
    return result

def sub(array: list) -> int:
    result = array[0]
    for i in array[1:]:
        result -= i
    return result


def custom_range(start, end, step, operation):
    result = []
    while start < end:
        result.append(start)
        start += step
    if operation == "+":
        return sum(result)
    elif operation == "*":
        return ...
    elif operation == "/":
        return ...
    elif operation == "-":
        return ...
    else:
        return "Not correct operation"