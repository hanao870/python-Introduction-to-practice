"""モジュール api の単体テスト."""
import unittest


class BuildUrlTest(unittest.TestCase):
    """モジュール `api` のユニットテストクラス."""

    def test_build_url(self) -> None:
        """`build_url()` のテスト."""
        from booksearch.api import build_url

        expected = "https://www.googleapis.com/books/v1/volumes?q=python"
        actual = build_url({"q": "python"})

        # アサーションメソッドの利用
        self.assertEqual(expected, actual)

    def test_build_url_empty_param(self) -> None:
        """`build_url()` のテスト. 空の書籍名を設定."""
        from booksearch.api import build_url

        expected = "https://www.googleapis.com/books/v1/volumes?"
        actual = build_url({})

        # アサーションメソッドの利用
        self.assertEqual(expected, actual)

    def test_build_url_fail(self) -> None:
        """`build_url()` の失敗テスト."""
        from booksearch.api import build_url

        expected = "https://www.googleapis.com/books/v1/volumes"
        actual = build_url({})

        # アサーションメソッドの利用
        self.assertEqual(expected, actual, msg="このテストは失敗します")
