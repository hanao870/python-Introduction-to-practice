"""モックオブジェクトの patch 動作確認."""
from unittest.mock import Mock, patch

import booksearch


@patch("booksearch.core.get_books")
def test_use_mock(mock_get_book: Mock) -> None:
    """`patch` のデコレータ使用例.

    Args:
        mock_get_book (Mock): モックオブジェクト

          関数呼び出し時に引数は不要
    """
    mock_get_book.return_value = []
    print(f"{booksearch.core.get_books(q='aaa')=}")


if __name__ == "__main__":
    # patch の第一引数にはドット('.')区切りの文字列を渡す
    with patch("booksearch.core.get_books") as mock_get_book:
        mock_get_book.return_value = []
        print(f"{booksearch.core.get_books(q='s')=}")

    test_use_mock()
