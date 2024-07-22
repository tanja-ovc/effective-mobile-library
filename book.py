import _csv
import csv

from books_data.utils import (
    CSVFILE_PATH, LATEST_BOOK_ID_FILE_PATH, new_or_empty_csvfile
)


class Book:
    """Класс книги с автогенерирующимся id и вводимыми пользователем
    названием, автором, годом издания и статусом.
    """

    def __init__(self, title: str, author: str, year: int, status: str):
        self.id: int = Book._generate_id()
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: str = status  # 'в наличии' или 'выдана'

    @staticmethod
    def _generate_id() -> int:
        book_id: int = 0
        with open(LATEST_BOOK_ID_FILE_PATH, 'r', encoding='utf-8') as file:
            reader: _csv.reader = csv.reader(file)
            rows: list = list(reader)  # Чтение всех строк в список
            if rows:
                first_row: list = rows[0]  # Получение последней строки
                first_value: str = first_row[0]  # Получение первого значения
                book_id: int = int(first_value) + 1
        with open(LATEST_BOOK_ID_FILE_PATH, 'w', encoding='utf-8') as file:
            writer: _csv.writer = csv.writer(file)
            writer.writerow(str(book_id + 1))
        return book_id

    @classmethod
    def from_list(cls, data):
        book = cls(data[1], data[2], int(data[3]), data[4])
        book.id = int(data[0])
        return book

    def to_list(self):
        return [self.id, self.title, self.author, self.year, self.status]

    def change_status(self, new_status: str):
        match new_status:
            case 'в наличии' | 'выдана':
                self.status: str = new_status
            case _:
                raise ValueError(
                    'Недопустимое значение для статуса книги. '
                    'Возможные значения: "в наличии", "выдана".'
                )

    def __str__(self):
        return f'#{self.id} "{self.title}", {self.author}, {self.year} г., {self.status}'
