import datetime
import sys

def creation():
    dict_books = []
    name = input("Название книги: ")
    author = input("Название автора: ")
    code = input("Уникальный код: ")
    for dicts in name, author, code:
        new_dict = {
            "Books": name,
            "name": author,
            'unic_code': code
            }
        dict_books.append(new_dict)
        return dict_books

def user_reader():
    list_1 = []
    ids = input("Ваше id: ")
    NAME = input("Ваше имя: ")
    USER_NAME = input("Ваша фамилия: ")
    for item in ids, NAME, USER_NAME:
        new_dict = {
            'id': ids,
            'name': NAME,
            'user_name': USER_NAME
        }
        list_1.append(new_dict)
        return list_1


def message():
    sms = """
Чтобы пройти регистрацию, вам нужно указать Имя и Фамилию, 
а так же id на ваш выбор, чтобы продолжить нажмите Enter """
    operation = input(sms)
    return operation

def choice_books():
    sms = """
Выберите книгу которая есть в наличии,
чтобы посмотреть список доступных книг, нажмите Enter"""
    operation = input(sms)
    return operation


def book_issue():
    book_list = creation()
    reader_list = user_reader()

    book_code = input("Введите код книги: ")
    reader_id = input("Введите ID читателя: ")

    date = datetime.datetime.now()
    sms_1 = f"Время фиксации {date} "
    print("Дата выдачи зафиксирована")
    sms_2 = f"Время фиксации {date}"

    book_info = next((book for book in book_list if book['unic_code'] == book_code), None)
    reader_info = next((reader for reader in reader_list if reader['id'] == reader_id), None)
    if book_info and reader_info:
        all_info = {
            'book_title': book_info['Books'],
            'book_author': book_info['name'],
            'reader_name': reader_info['name'],
            'reader_surname': reader_info['user_name'],
            'issue_date': sms_1,
            'return_date': sms_2
        }
        return all_info
    else:
        print("Книга или читатель не найдены.")
        return None

while True:
    print("Выберите действие:")
    print("1. Создать книгу")
    print("2. Зарегистрировать читателя")
    print("3. Выдать книгу")
    print("4. Выход")

    choice = input("Введите номер действия: ")

    if choice == "1":
        creation()
    elif choice == "2":
        user_reader()
    elif choice == "3":
        book_issue()
    elif choice == "4":
        print("Выход из программы...")
        sys.exit()
    else:
        print("Неверный выбор. Попробуйте еще раз.")