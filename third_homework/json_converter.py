import json
import csv


def json_converter():
    with open('converted_file.csv') as books:
        book_list = []
        csv_reader = csv.DictReader(books)
        for row in csv_reader:
            book_list.append(row)
    return book_list


def write_book_json(book_list):
    with open('books.json', 'w') as books_json:
        json.dump(book_list, books_json, indent=4)


def read_book_dict_json():
    with open('books.json') as books_dictionary_json:
        books_data = json.load(books_dictionary_json)
    return books_data


def read_user_dict_json():
    with open('users.json', 'r') as user_json:
        users_data = json.load(user_json)
    return users_data


def iter_books(books_data):
    for book in books_data:
        yield book


def iter_users(users_data):
    for user in users_data:
        users = {
            'name': user["name"],
            'gender': user["gender"],
            'address': user["address"],
            'age': user["age"],
        }
        yield users


def add_book_to_user(books_data, users_data):
    fun_book = iter_books(books_data)
    fun_user = iter_users(users_data)
    draft_user = []
    for i in range(len(books_data)):
        try:
            book_dict = next(fun_book)
            user = next(fun_user)
            dictionary_copy = user.copy()
            dictionary_copy["books"] = [book_dict]
            draft_user.append(dictionary_copy)
        except StopIteration:
            try:
                for i in draft_user:
                    other_books = next(fun_book)
                    i['books'].append(other_books)
            except StopIteration:
                pass
    with open('result.json', 'w') as result:
        json.dump(draft_user, result, indent=4)
