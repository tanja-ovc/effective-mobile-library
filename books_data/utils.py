import os


CSVFILE_PATH: str = 'books_data/books.csv'
LATEST_BOOK_ID_FILE_PATH = 'books_data/latest_book_id.csv'

new_or_empty_csvfile: bool = (
        not os.path.exists(CSVFILE_PATH)
        or os.stat(CSVFILE_PATH).st_size == 0
    )
