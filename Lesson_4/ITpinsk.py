# for i in range(1, 10):
#     for j in range(2,10):
#         print(f"{i} * {j} = {i * j}")
#     print()

# n = input("Число: ")
# while n != 'exit':
#     if int(n) % 2 == 0:
#         print("Чет")
#     else:
#         print("Нечет")
#     n = input("Число или exit: ")

# a = [1, 2.5, 'asdnsa', ('a', 'b', 'c'), 225]
# a_int = []
# for item in a:
#     if isinstance(item, int):  #if type(item) == int:
#         a_int.append(item)
# print(a_int)


# f_1, f_2 = 1, 1
# print(f_1,f_2)
# for _ in range(9):
#     f_1, f_2 = f_2, f_1 + f_2
#     print(f_1)

# km_h = {'speed_1': 100,
#         'speed_2': 92,
#         'speed_3': 132,
#         'speed_4': 46
#         }
# m_h = dict()
# km_h_items = km_h.items()
# print(km_h_items)
# for k,v in km_h_items:
#     m_h[k] = v * 1.609
# print(m_h)
  # km_h.items()
 # Цикл for by items
 # km_h in m_h
 # Using dict comprehension
 # M/H = Km/H * 1.609
# m_h = {k: v * 1609 for k,v in km_h.items()}
# print(m_h)

# color = (12, 43, 54, 13)
# match color:
#     case (r, g, b):
#         print(f"r - {r}, g - {g}, b - {b}")
#     case (r, g, b, a):
#         print(f"r - {r}, g - {g}, b - {b}, a - {a}")
#     case _:
#         print("not correct")

# n = int(input("Число: "))
# for i in range(1, 11):
#     if n == i:
#         print(end='')
#     print(f"{n} * {i} = {n * i}")

# for i in range(65,91):
#     print(chr(i), end='\t')


# a = [5, 4, 3, 4, 1, 2, 2]
# for i in range(len(a) - 1):
#     for j in range(len(a) - 1 - i):
#         if a[j] < a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
# print(a)



text = 'the_stealth-warrior'
text_one = text.replace("-", " ") and text.replace("_", " ")
print(text_one)

# res = array.wsplit()[0] + ''.join([w.capitalize() for w in array.split()[1:]])
# print(res)