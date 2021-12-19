import json
import itertools
import random
from typing import Iterator

from faker import Faker

from conf import MODEL

J = 'output1.json'


def model() -> str:
    """
    генерирует модель
    :return: модель
    """
    return MODEL


def title() -> str:
    """
    генерирует названия книг из файла books.txt
    :return: название книги
    """
    titles = 'books.txt'
    with open(titles, encoding='utf8') as f:
        iter_ = itertools.cycle(f)
        for _ in range(random.randint(1, 100)):
            a = next(iter_)
    return a.rstrip()


def year() -> int:
    """
    генерирует год выпуска книги
    :return: год выпуска
    """
    return random.randint(1900, 2021)


def pages() -> int:
    """
    генерирует количество страниц
    :return: количество страниц
    """
    return random.randint(10, 5000)


def isbn13() -> str:
    """
    генерирует международный стандартный книжный номер
    :return: международный стандартный книжный номер
    """
    fake = Faker()
    return fake.isbn13()


def rating() -> float:
    """
    генерирует место в рейтинге
    :return: место в рейтинге
    """
    return round(random.uniform(0, 5), 1)


def price() -> float:
    """
    генерирует стоимость
    :return: стоимость
    """
    return round(random.uniform(100.0, 5000.9), 2)


def author() -> list:
    """
    генерирует список авторов от одного до трех
    :return: список авторов
    """
    fake = Faker()
    autors_list = [fake.name() for _ in range(random.randint(1, 3))]
    return autors_list


def gen(pk=1) -> Iterator[dict]:
    """
   генерирует итератор словаря с данными книги
    :return:
    """

    while True:
        dict_book = {
            "model": model(),
            "pk": pk,
            "fields": {
                "title": title(),
                "year": year(),
                "pages": pages(),
                "isbn13": isbn13(),
                "rating": rating(),
                "price": price(),
                "author": author()
            }
        }
        yield dict_book
        pk += 1


def json_gen(fn):
    """
    Декоратор преобразует вывод функции в json файл output1.json
    :return: запись в файле json
    """

    def wrapper(n):
        with open(J, 'w', encoding='utf8') as f:
            json.dump(fn(n), f, indent=4, ensure_ascii=False)

    return wrapper


@json_gen
def list_gen(n: int) -> list:
    """
    Вызывает итератор генератора словаря n раз и создаёт список словарей с данными книг
    :return: список словарей с данными книг
    """
    list_books = []
    a = gen()
    for i in range(n):
        list_books.append(next(a))
    print(list_books)
    return list_books


def main():
    """
    вызывает генератор списка словарей книг  100 раз и записывает результат в json файл output1.json
    :return: список словарей книг, заполненный json файл
    """
    return list_gen(100)


if __name__ == "__main__":
    main()
