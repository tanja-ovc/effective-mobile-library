from book import Book
from book_actions import (
    all_books, change_book_status, create_book, delete_book, search_books
)
from validators import (
    book_id_exists, validate_value_or_break_command
)


def all_commands() -> None:
    print('\nДоступные команды:'
          '\n- добавить книгу'
          '\n- показать все книги'
          '\n- найти книги'
          '\n- изменить статус книги',
          '\n- удалить книгу'
          '\n- прервать команду (при запущенной команде)'
          '\n- показать все команды'
          '\n- выйти')


def start_commands() -> None:
    all_commands()

    while True:
        command: str = input('\nВведите команду: ').strip().lower()

        match command:
            case 'выйти':
                break

            case 'показать все команды':
                all_commands()

            case 'добавить книгу':
                title: str = input('Введите название: ')
                author: str = input('Введите имя автора: ')
                year_input_msg: str = 'Введите год издания: '
                year: str = input(year_input_msg)

                year: str = validate_value_or_break_command(
                    value=year,
                    pattern=r'^\d{4}$',
                    error_msg=('\nОШИБКА: Год должен состоять из 4 цифр. '
                               'Повторите ввод либо введите "прервать команду".'),
                    input_msg=year_input_msg
                )
                if year == 'прервать команду':
                    print('\nКоманда прервана.')
                    continue

                create_book(title=title,
                            author=author,
                            year=int(year),
                            status='в наличии')

                print('\nКнига успешно добавлена.')

            case 'показать все книги':
                print()
                for book in all_books():
                    print(book)

            case 'найти книги':
                search_field_msg: str = 'Введите поле для поиска: '
                search_field: str = input(search_field_msg).strip().lower()

                search_field: str = validate_value_or_break_command(
                    value=search_field,
                    pattern='^(название|автор|год)$',
                    error_msg=('\nОШИБКА: неверное название поля для поиска. '
                               'Допустимые варианты: "название", "автор", "год".'
                               '\nПовторите ввод либо введите "прервать команду".'),
                    input_msg=search_field_msg
                )
                if search_field == 'прервать команду':
                    print('\nКоманда прервана.')
                    continue

                keyword: str = input('Введите ключевое слово для поиска: ').strip().lower()

                books: list[Book] | None = search_books(search_field, keyword)
                if books is not None and books:
                    print('\nНайденные книги:')
                    for book in books:
                        print(book)
                else:
                    print('\nКниги не найдены.')

            case 'изменить статус книги':
                book_id_input_msg: str = 'Введите id книги: '
                book_id: str = input(book_id_input_msg)

                book_id: str = validate_value_or_break_command(
                    value=book_id,
                    pattern=r'^\d+$',
                    error_msg=('\nОШИБКА: id книги должен быть целым числом. '
                               'Повторите ввод либо введите "прервать команду".'),
                    input_msg=book_id_input_msg)

                if book_id == 'прервать команду':
                    print('\nКоманда прервана.')
                    continue

                while not book_id_exists(book_id):
                    print('\nОШИБКА: Нет книги с таким id. '
                          'Повторите ввод либо введите "прервать команду".')
                    book_id: str = input(book_id_input_msg)
                    if book_id == 'прервать команду':
                        break
                if book_id == 'прервать команду':
                    print('\nКоманда прервана.')
                    continue

                new_status_msg: str = 'Введите новый статус книги: '
                new_status: str = input(new_status_msg)

                status: str = validate_value_or_break_command(
                    value=new_status,
                    pattern='^(в наличии|выдана)$',
                    error_msg=('\nОШИБКА: Недопустимое значение для статуса книги. '
                               'Возможные значения: "в наличии", "выдана".'
                               '\nПовторите ввод либо введите "прервать команду".'),
                    input_msg=new_status_msg)

                change_book_status(int(book_id), status)

                print('\nСтатус книги успешно изменён.')

            case 'удалить книгу':
                book_id_input_msg: str = 'Введите id книги для удаления: '
                book_id: str = input(book_id_input_msg)

                book_id: str = validate_value_or_break_command(
                    value=book_id,
                    pattern=r'^\d+$',
                    error_msg=('\nОШИБКА: id книги должен быть целым числом. '
                               'Повторите ввод либо введите "прервать команду".'),
                    input_msg=book_id_input_msg
                )
                if book_id == 'прервать команду':
                    print('\nКоманда прервана.')
                    continue

                while not book_id_exists(book_id):
                    print('\nОШИБКА: Нет книги с таким id. '
                          'Повторите ввод либо введите "прервать команду".')
                    book_id: str = input(book_id_input_msg)
                    if book_id == 'прервать команду':
                        break
                if book_id == 'прервать команду':
                    print('\nКоманда прервана.')
                    continue

                delete_book(int(book_id))

                print('\nКнига успешно удалена.')

            case _:
                print('ОШИБКА: неизвестная команда')


if __name__ == '__main__':
    start_commands()
