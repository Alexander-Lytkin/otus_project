import names
from numpy import random


def random_first_name():
    return names.get_first_name()


def random_second_name():
    return names.get_last_name()


def random_email():
    email = ''
    for _ in range(7):
        letter = random.randint(999)
        email += str(letter)

    email += '@gmail.com'
    return email


def random_phone():
    phone = ''
    for _ in range(8):
        num = random.randint(10)
        phone += str(num)
    return phone


def random_password():
    password = ''
    for _ in range(8):
        num = random.randint(10)
        password += str(num)
    return password
