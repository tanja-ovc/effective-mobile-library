from __future__ import annotations


class Book:
    """Класс книги с автогенерирующимся id и вводимыми пользователем
    названием, автором, годом издания и статусом.
    """

    def __init__(self,
                 id: int,
                 title: str,
                 author: str,
                 year: int,
                 status: str):

        self.id: int = id
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: str = status  # 'в наличии' или 'выдана'

    @classmethod
    def from_list(cls, data) -> Book:
        book: Book = cls(data[0], data[1], data[2], int(data[3]), data[4])
        return book

    def to_list(self) -> list:
        return [self.id, self.title, self.author, self.year, self.status]

    def __str__(self) -> str:
        return f'#{self.id} "{self.title}", {self.author}, {self.year} г., {self.status}'
