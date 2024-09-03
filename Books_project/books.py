import datetime

BOOK_DB = {}
RENTED_DB = {}
READER_DB = {}
AVAILABLE_BOOKS_DB = {}
DEALS_DB = {}

def save_book(book):
    if book["code"] in BOOK_DB:
        print(f"Книга с кодом {book['code']} уже существует.")
    else:
        BOOK_DB[book["code"]] = book
        AVAILABLE_BOOKS_DB[book["code"]] = book

def create_book():
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    book_code = input("Введите уникальный код книги: ")
    book = {"author": author, "code": book_code, "title": title}
    save_book(book)

def register_reader():
    reader_id = input("Введите Ваше ID: ")
    first_name = input("Введите Ваше имя: ")
    last_name = input("Введите Вашу фамилию: ")
    reader = {"id": reader_id, "first_name": first_name, "last_name": last_name}
    READER_DB[reader_id] = reader

def book_issue():
    book_code = input("Введите код книги: ")
    reader_id = input("Введите ID читателя: ")

    if book_code in AVAILABLE_BOOKS_DB and reader_id in READER_DB:
        book = AVAILABLE_BOOKS_DB.pop(book_code)
        RENTED_DB[book_code] = book
        DEALS_DB[f"{reader_id}_{book_code}"] = {
            "book_title": book["title"],
            "book_author": book["author"],
            "reader_id": reader_id,
            "issue_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "return_date": None
        }
        print("Книга успешно выдана.")
    else:
        print("Книга или читатель не найдены.")

while True:
    print("Выберите действие:")
    print("1. Создать книгу")
    print("2. Зарегистрировать читателя")
    print("3. Выдать книгу")
    print("4. Выход")

    choice = input("Введите номер действия: ")

    if choice == "1":
        create_book()
    elif choice == "2":
        register_reader()
    elif choice == "3":
        book_issue()
    elif choice == "4":
        print("Выход из программы...")
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")