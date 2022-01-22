from third_homework.csv_writer import csv_writer
from third_homework.deleter import delete_all_tmp_files
from third_homework.json_converter import json_converter
from third_homework.parser_html import scv_parser

tmp_files = ["books.csv", "books.json", "converted_file.csv", "raw_csv_book.csv", "users.json"]

if __name__ == '__main__':
    scv_parser()
    csv_writer()
    json_converter()
    delete_all_tmp_files(tmp_files)
