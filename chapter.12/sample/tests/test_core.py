"""モジュール core の単体テスト."""
import pathlib
import unittest
from tempfile import TemporaryDirectory
from unittest.mock import Mock, patch
from urllib.error import URLError

THUMBNAIL_URL = (
    "http://books.google.com/books/content"
    "?id=OgtBw76OY5EC&printsec=frontcover"
    "&img=1&zoom=1&edge=curl&source=gbs_api"
)


class SaveThumbnailsTest(unittest.TestCase):
    """モジュール core の単体テストクラス."""

    def setUp(self) -> None:
        """テスト準備.

        テストメソッド実行前に毎回呼ばれる.

        `setUp` でエラーが発生すると、テスト失敗となる
        """
        # 一時ディレクトリを作成
        self.tmp = TemporaryDirectory()

    def tearDown(self) -> None:
        """テストの後片付け.

        テストメソッド実行後、結果が記録された直後に呼ばれる.

        この関数はテストメソッドで例外が発生しても呼び出される.
        """
        # 一時ディレクトリを破棄
        self.tmp.cleanup()

    def test_save_thumbnails(self) -> None:
        """`Book` クラスの `save_thumbnails()` 関数の単体テスト."""
        from booksearch.core import Book

        book = Book(
            {"id": "", "volumeInfo": {"imageLinks": {"thumbnail": THUMBNAIL_URL}}}
        )

        # 処理を実行し、ファイルが作成されることを確認する
        filename = book.save_thumbnails(self.tmp.name)[0]
        self.assertTrue(pathlib.Path(filename).exists())

    @patch("booksearch.core.get_data")
    def test_save_thumbnails_using_patch(self, mock_get_data: Mock) -> None:
        """モックオブジェクトのパッチを使用した`Book` クラスの `save_thumbnails()` 関数の単体テスト."""
        from booksearch.core import Book

        # 事前に取得したサムネイル画像データをモックの戻り値にセット
        data_path = pathlib.Path(__file__).with_name("data")
        mock_get_data.return_value = (data_path / "_thumbnail.jpeg").read_bytes()

        book = Book(
            {"id": "", "volumeInfo": {"imageLinks": {"thumbnail": THUMBNAIL_URL}}}
        )

        filename = book.save_thumbnails(self.tmp.name)[0]

        # get_data() 呼び出し時の引数確認
        mock_get_data.assert_called_with(THUMBNAIL_URL)

        # 保存されたテストデータを確認
        self.assertEqual(mock_get_data.return_value, filename.read_bytes())


class GetBooksTest(unittest.TestCase):
    """モジュール `core` の単体テストクラス."""

    def test_get_books_no_connection(self) -> None:
        """`get_books` の単体テスト.

        通信失敗の例外発生をテストする
        """
        from booksearch.core import get_books

        # 一時的にネットワークアクセスを遮断
        with patch("socket.socket.connect") as mock:
            # connect が呼び出された際に不正な値を返す
            mock.return_value = None

            with self.assertRaisesRegex(URLError, "urlopen error"):
                # 例外が発生する処理を with ブロック内で実行する
                get_books(q="python")


class BuildUrlMultiTest(unittest.TestCase):
    """モジュール `core` の単体テストクラス."""

    def test_build_url_multi(self) -> None:
        """`build_url` の単体テスト."""
        from booksearch.api import build_url

        base = "https://www.googleapis.com/books/v1/volumes?"
        expected_url = f"{base}q=python"

        # 2, 3 番目のテストは失敗する
        params = (
            (expected_url, {"q": "python"}),
            (expected_url, {"q": "python", "maxResult": 1}),
            (expected_url, {"q": "python", "langRestrict": "en"}),
        )

        for expected, param in params:
            with self.subTest(param):
                actual = build_url(param)
                self.assertEqual(expected, actual)
