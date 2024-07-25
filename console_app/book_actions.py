import _csv
import csv
import os

from book import Book

DATA_FILE_PATH: str = 'books_data/books.txt'
LAST_ID_FILE_PATH: str = 'books_data/last_id.txt'


def create_book(title: str,
                author: str,
                year: int,
                status: str) -> None:
    """Создаёт объект класса книги и записывает данные о созданном
    объекте в текстовый файл.
    """

    book_id = 1
    new_or_empty_id_file: bool = (
            not os.path.exists(LAST_ID_FILE_PATH)
            or os.stat(LAST_ID_FILE_PATH).st_size == 0
    )
    if not new_or_empty_id_file:
        with open(LAST_ID_FILE_PATH, mode='r') as id_file:
            book_id = int(id_file.read().strip()) + 1

    book: Book = Book(id=book_id,
                      title=title,
                      author=author,
                      year=year,
                      status=status)

    with open(DATA_FILE_PATH, 'a', encoding='utf-8') as data_file:
        writer: _csv.writer = csv.writer(data_file)
        writer.writerow(book.to_list())

    with open(LAST_ID_FILE_PATH, mode='w', encoding='utf-8') as id_file:
        id_file.write(str(book_id))


def all_books() -> list[Book]:
    """Возвращает все объекты книг из текстового файла."""

    with open(DATA_FILE_PATH, 'r', encoding='utf-8') as data_file:
        reader: _csv.reader = csv.reader(data_file)
        books: list[Book] = [Book.from_list(row) for row in reader]
        return books


def search_books(search_field: str, keyword: str) -> list[Book] | None:
    """Возвращает результат поиска книг по заданным полям и ключевым словам."""

    books: list[Book] = all_books()
    match search_field:
        case 'название':
            return [book for book in books if keyword.lower() in book.title.lower()]
        case 'автор':
            return [book for book in books if keyword.lower() in book.author.lower()]
        case 'год':
            return [book for book in books if str(book.year) == keyword]
        case _:
            return None


def change_book_status(book_id: int, new_status: str) -> None:
    """Меняет статус книги по её id."""

    books: list[Book] = all_books()
    for book in books:
        if int(book.id) == book_id:
            book.status = new_status
    with open(DATA_FILE_PATH, 'w', encoding='utf-8') as data_file:
        writer: _csv.writer = csv.writer(data_file)
        for book in books:
            writer.writerow(book.to_list())


def delete_book(book_id: int) -> None:
    """Удаляет книгу по её id."""

    books: list[Book] = [book for book in all_books() if int(book.id) != book_id]
    with open(DATA_FILE_PATH, 'w', encoding='utf-8') as data_file:
        writer: _csv.writer = csv.writer(data_file)
        for book in books:
            writer.writerow(book.to_list())
