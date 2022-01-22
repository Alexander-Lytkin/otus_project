import json
import csv


def json_converter():
    with open('converted_file.csv') as books:
        book_list = []
        csv_reader = csv.DictReader(books)
        for row in csv_reader:
            book_list.append(row)

    with open('books.json', 'w') as books_json:
        json.dump(book_list, books_json, indent=4)

    with open('books.json') as books_dictionary_json:
        books_data = json.load(books_dictionary_json)
        users_with_books = []

    with open('users.json', 'r') as user_json:
        users_data = json.load(user_json)

    def gen_func():
        for user in users_data:
            yield user

    fun = gen_func()

    for book in books_data:
        try:
            user = next(fun)
        except StopIteration:
            fun = gen_func()

        data = {'name': user["name"],
                'gender': user["gender"],
                'address': user["address"],
                'age': user["age"],
                'books': [
                    {'title': book["Title"],
                     'author': book["Author"],
                     "pages": book["Pages"],
                     "genre": book["Genre"],
                     }]
                }
        users_with_books.append(data)

    with open('result.json', 'w') as result:
        json.dump(users_with_books, result, indent=4)
