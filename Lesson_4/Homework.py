# Задача 1
# a = list(filter(lambda x: (x % 2 == 0), [1, 2, 3, 4, 5, 6]))
# print(a)

# Задача 2
# a = lambda x: x + x
# print(a(5))

# Задача 3

# a = list(filter(lambda x: len(x) > 3, ['1', '124asdsa', 'as', 'sa213sdass']))
# print(a)

# Задача 4
# a = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5, 6]))
# print(a)


# Задача 5

# a = list(filter(lambda x: x.lower().startswith('a'), ['123', 'asdsadsa', 'gsdfe', 'sad213', 'Anatoli']))
# print(a)

# Задача 6
# a = list(filter(lambda x: x > 10, [4, 2, 6, 3, 1, 16, 13, 20, 7]))
# print(a)

# Задача 7
# l = ['tron', 'asd31as', 'dsadsadsa','tolik']
# a = list(map(lambda x: x.upper(), l))
# print(a)

# Задача 8
# a = list(filter(lambda x: (x % 3 == 0), range(1, 30)))
# print(a)

# Задача 9

# a = list(filter(lambda x: x < 10 and x > 5, range(1, 15)))
# print(a)

# Задача 10
# a = list(filter(lambda x: x.lower().endswith('o'), ['asedwq', 'wqeuooo', '1235asdsdoo', 'Gronto']))
# print(a)

# Задача 1 лист
# l = ['1324', 'sdsawq', 'sdaasxxzfdw12', 'asdas21a','123']
# def symbol(arr: str) -> list:
#     return [sym for sym in arr if len(sym) > 5]
# print(symbol(l))


# l = ['1324', 'sdsawq', 'sdaasxxzfdw12', 'asdas21a','123']
# a = [i for i in l if len(i) > 5]
# print(a)

# Задача 2 лист


def sqr_d():
    dicts = dict()
    for i in range(1, 11):
        dicts[i] = i
        if i % 2 != 0:
            dicts[i] = i ** 2
    return dicts
print(sqr_d())

dict1 = {1:1, 2:2, 3:3, 4:4, 5:5,
         6:6, 7:7, 8:8, 9:9, 10:10}
dict2 = {k: v**2 for (k, v) in dict1.items() if v % 2 != 0}
print(dict2)

# Задача 3 лист

# Задача 4 лист

# a = [i**3 for i in range(1, 11)]
# print(str(a).replace("64", 'Four').replace('512', 'Four'))

# Задача 5 лист
