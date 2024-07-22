import _csv
import csv

from book import Book
from books_data.utils import CSVFILE_PATH, new_or_empty_csvfile


def create_book(title: str, author: str, year: int, status: str) -> None:
    """Создаёт объект класса книги и записывает данные о созданном
    объекте в csv-файл.
    """

    book: Book = Book(title=title, author=author, year=year, status=status)

    with open(CSVFILE_PATH, 'a', encoding='utf-8') as csvfile:
        writer: _csv.writer = csv.writer(csvfile)
        if new_or_empty_csvfile:
            writer.writerow(['id', 'title', 'author', 'year', 'status'])
        writer.writerow(book.to_list())


def read_all_books() -> list[Book]:
    with open(CSVFILE_PATH, 'r', encoding='utf-8') as csvfile:
        reader: _csv.reader = csv.reader(csvfile)
        books: list = [str(Book.from_list(row)) for row in reader]
        return books
