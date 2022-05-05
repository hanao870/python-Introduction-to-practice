"""サンプルテストモジュール."""
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
