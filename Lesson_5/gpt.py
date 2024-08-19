# 1
def calculator(first, second, operation):
    if operation == '+':
        return (first + second)
    elif operation == '-':
        return (first - second)
    elif operation == '*':
        return (first * second)
    if operation == '/':
        return (first / second)
    else:
        print("Неизвестная операция!")
    return operation

def dopolnen():
    message = """
Какую вы бы операцию хотели бы сделать выбери из списка:
Умножение *
Деление /
Вычитание -

Сложение +

Ваш выбор: """
    operation = input(message)
    print()
    return operation

def open_calcul():
    try:
        a = int(input("Введите 1 число: "))
        b = int(input("Введите 2 число: "))
        dopol = dopolnen()
        result = calculator(a, b, dopol)
        print(f"Результат калькулятора: {result}")
    except ValueError:
        print("Вы завершили операцию")
while True:
    if open_calcul() != 'exit':
        break

open_calcul()

#
# func(2)