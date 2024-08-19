import time
from datetime import datetime
from time import sleep


# def decorator(func):
#     def wrapper():
#         print("Загрузка")
#         time.sleep(2)
#         func()
#         print("Финиш")
#     return wrapper()
#
# #
# @decorator
# def say_hello():
#     print('Hello')



#
# def loger(func):
#     def wrapper(*args, **kwargs):
#         print(f"Время начало работы, {datetime.now}{func.__name__}")
#         res = func(*args, **kwargs)
#         print('время окончания работы', datetime.now())
#         return res
#     return wrapper
#
#
# @loger
# def say_hello(name):
#     print(f"Hello {name}")
#
#
#
# def user_admin(func):
#     def wrapper(user_type):
#         res = ['admin', 'user']
#         if user_type not in res:
#             return "denied"
#         return func(user_type)
#     return wrapper
#
# @user_admin
def admin(user_type):
    res = ['admin','user']
    if user_type not in res:
        return 'denied'
    return 'access'

print(admin('admin'))
print(admin('user'))
print(admin('asdadjaksdja'))

def decorator(func):
    def wrap(x,y):
        ann = func.__annotations__
        if type(x) != ann['x'] or type(y) != ann['y']:
            return False
        return True
    return wrap

@decorator
def do_smth(x: int, y: str):
    sleep(2)

print(do_smth(1, 'as'))


def cache_three(func):
    counter, cache = 0, dict()
    def wrap(x):
        nonlocal counter
        counter += 1