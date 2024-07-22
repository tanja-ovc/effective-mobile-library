import re

from book_actions import create_book, read_all_books


print('\nДоступные команды:'
      '\n- добавить книгу'
      '\n- показать все книги',
      '\n...'
      '\n- выйти')


def start_app() -> None:
    while True:
        command = input('\nВведите команду: ').strip().lower()

        match command:
            case 'выйти':
                break

            case 'добавить книгу':
                title: str = input('Введите название: ')
                author: str = input('Введите имя автора: ')
                year: str = input('Введите год издания: ')

                year_is_4_digits: re.Match | None = re.fullmatch(r'^\d{4}$', year)
                while year_is_4_digits is None:
                    print('\nОШИБКА: Год должен состоять из 4 цифр. Попробуйте снова.')
                    year = input('Введите год издания: ')
                    year_is_4_digits: re.Match | None = re.fullmatch(r'^\d{4}$', year)

                create_book(title=title,
                            author=author,
                            year=int(year),
                            status='в наличии')
                print('\nКнига успешно добавлена.')

            case 'показать все книги':
                print()
                for book in read_all_books():
                    print(book)

            case _:
                print('ОШИБКА: неизвестная команда')


if __name__ == '__main__':
    start_app()
