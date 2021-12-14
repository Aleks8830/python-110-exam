from conf import model
import random
from random import randint, uniform
from faker import Faker
import json

faker = Faker()


def main():
    book = gen(1)
    list_1 = [next(book) for i in range(100)]
    print(list_1)
    output_file = "output_3.txt"
    with open(output_file, "w", encoding='utf-8') as f:
        json.dump(list_1, f, ensure_ascii=False, indent=4)


def title() -> str:
    """функция возв название книги"""
    books_file = "books.txt"
    with open(books_file, encoding="utf-8") as f:
        line = f.readline()
        line_title = random.choice(line)
        return line_title


def year(start_year=1900, end_year=2021) -> int:
    """

    :param start_year:
    :param end_year:
    :return:
    """
    return randint(start_year, end_year)


def get_pages() ->int:
    return randint(0, 100)


def isbn13() ->str:
    return faker.isbn13()


def get_autor() ->list[str]:
    return faker.name()


def get_rating() ->int:
    return uniform(0.0, 5.0)


def get_price() ->int:
    price_cur = uniform(5.0, 1000.0)
    return price_cur


def gen(pk=1) ->dict:
    while True:
        yield {
            "model": model,
            "pk": pk,
            "fields": {
                "title": title(),
                "pages": get_pages(),
                "isbn13": isbn13(),
                "rating": get_rating(),
                "price": get_price(),
                "author": get_autor()

            }
        }
        pk = pk + 1


if __name__ == "__main__":
    main()

