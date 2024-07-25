import re

from book import Book
from book_actions import all_books


def book_id_exists(book_id: str) -> bool:
    """Проверят, существует ли id книги в текстовом файле."""

    books: list[Book] = all_books()
    book_ids: list = [book.id for book in books]
    if book_id in book_ids:
        return True
    return False


def validate_value_or_break_command(value: str,
                                    pattern: str,
                                    error_msg: str,
                                    input_msg: str) -> str:
    """Валидирует вводимые пользователем значения, а также
    позволяет прервать команду в случае безуспешного ввода.
    """

    value_match: re.Match | None = re.fullmatch(pattern, value)
    while value_match is None:
        print(error_msg)
        value: str = input(input_msg)
        if value == 'прервать команду':
            break
        value_match: re.Match | None = re.fullmatch(pattern, value)
    return value
