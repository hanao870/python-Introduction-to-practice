"""モックオブジェクトの patch 動作確認."""
from unittest.mock import patch

import booksearch

if __name__ == "__main__":
    with patch("booksearch.core.get_books") as mock_get_book:
        mock_get_book.return_value = []
        print(f"{booksearch.core.get_books(q='s')=}")
