"""モジュール api の単体テスト."""
import sys
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

    # テスト失敗時の結果を抑制する
    # 一時的な対応時(リファクタリング等)に使用.
    @unittest.expectedFailure
    def test_build_url_fail(self) -> None:
        """`build_url()` の失敗テスト."""
        from booksearch.api import build_url

        expected = "https://www.googleapis.com/books/v1/volumes"
        actual = build_url({})

        # アサーションメソッドの利用
        self.assertEqual(expected, actual, msg="このテストは失敗します")

    # 引数にスキップする理由を渡す
    @unittest.skip("this is a skip test")
    def test_nothing_skip(self) -> None:
        """テストスキップの動作確認."""
        pass

    # Python バージョンが 3.6 より大きければスキップ
    @unittest.skipIf(sys.version_info > (3, 6), "this is a skipIf test")
    def test_nothing_skipIf(self) -> None:
        """条件付きテストスキップの動作確認."""
        pass
