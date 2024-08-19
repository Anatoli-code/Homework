# from datetime import datetime
#
# # def decorator(func):
# #     def wrapper(name):
# #         print("Ща будеь хелло")
# #         c = func(name)
# #         print("Был хелло")
# #         return c
# #     return wrapper
# #
# # @decorator
# # def hello(name):
# #     print(f'Hello {name}')
# #
# # hello("TOlike")
#
#
#
# def benchmark(func):
#     def wrap():
#         start = datetime.now()
#         func()
#         return datetime.now() - start
#     return wrap()
#
# @benchmark
# def get_list_1():
#     [i for i in range(10_000)]
#
# @benchmark
# def get_list_2():
#     lst = []
#     for i in range(10_000):
#         lst.append(i)
#
# print("list compehension", get_list_1())
# print("list append metod", get_list_2())





def dec_upper(func):
    def wrapper(l:str) -> str:
        res = l.upper()
        return res
    return wrapper

@dec_upper
def n(name):
    return n

print(n("tolik"))


def dec_value(func):
    def wrraper():
        try:
            func()
        except Exception as e:
            return e
    return wrraper

@dec_value
def t():
    c = [1, 2, 3]
    a = c[6]
    return c

print(t())


dict_1 = {
    "Ножницы": 'Бумага',
    'Камень': "Ножницы",
    "Бумага": "Камень"
}

def game(play_1: str, play_2: str) ->dict:
    if play_1[dict_1] > play_2:
        return "play 1 win"
    elif play_2[dict_1] > play_1:
        return "play 2 win"
    elif play_1 == play_2:
        return "Ничья"

game("Ножницы", "Бумага")