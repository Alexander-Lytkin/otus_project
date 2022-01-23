from third_homework.csv_writer import csv_writer
from third_homework.deleter import delete_all_tmp_files
from third_homework.json_converter import json_converter, write_book_json, read_book_dict_json, read_user_dict_json, \
    add_book_to_user
from third_homework.parser_html import scv_parser

tmp_files = ["books.csv", "books.json", "converted_file.csv", "raw_csv_book.csv", "users.json"]

if __name__ == '__main__':
    scv_parser()
    csv_writer()
    book_list = json_converter()
    write_book_json(book_list)
    books_data = read_book_dict_json()
    users_data = read_user_dict_json()
    add_book_to_user(books_data, users_data)
    delete_all_tmp_files(tmp_files)
