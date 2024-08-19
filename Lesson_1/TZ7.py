calendar = int(input("Enter your number: "))
if (calendar % 4 == 0 and calendar % 100 != 0) or calendar % 400 == 0:
    print("Год високосный: ")
else:
    print("Год не високосный: ")