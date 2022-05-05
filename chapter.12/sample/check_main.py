"""パッケージの動作確認用モジュール."""
from booksearch.core import get_books

if __name__ == "__main__":
    books = get_books(q="python")

    for book in books:
        print(book)
