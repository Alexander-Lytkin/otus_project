import os

import pandas as pd
from bs4 import BeautifulSoup

users = "curl -o /home/al/PycharmProjects/OTUS/otus_project/third_homework/users.json https://raw.githubusercontent.com/konflic/front_example/master/data/users.json"
books = "curl -o /home/al/PycharmProjects/OTUS/otus_project/third_homework/books.csv https://github.com/konflic/front_example/blob/master/data/books.csv"

os.system(users)
os.system(books)


def scv_parser():
    data = []
    list_header = []
    soup = BeautifulSoup(open('books.csv', 'r'), 'html.parser')
    header = soup.find_all("table")[0].find("tr")

    for items in header:
        try:
            list_header.append(items.get_text())
        except:
            continue

    html_data = soup.find_all("table")[0].find_all("tr")[1:]

    for element in html_data:
        sub_data = []
        for sub_element in element:
            try:
                sub_data.append(sub_element.get_text())
            except:
                continue
        data.append(sub_data)

    dataFrame = pd.DataFrame(data=data, columns=list_header)
    dataFrame.to_csv('raw_csv_book.csv')
