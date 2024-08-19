def compas(comp):
    x, y = 0,0
    for value in comp:
        if value == 'S':
            y -= 1
        elif value == 'W':
            x -= 1
        elif value == 'E':
            x += 1
        elif value == 'N':
            y += 1
    return (x,y)

i = input("Введите букву S,W,E,N: ")


def control_error(user):
    if user == '':
        print("Вы ничего не ввели!")
    elif user == float and int:
        print("Числа нельзя и любые другие символы нельзя")
    return user
# print(compas(control_error(comp)))

def print_go(c: str):
    if len(c) < 100 and len(c) >= 1:
        print("It's okey" )
    else:
        print("Problem")
    return c

print(compas(control_error(print_go(i))))