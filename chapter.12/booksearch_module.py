"""unit test サンプル."""
import unittest


def book_search() -> dict[None, None]:
    """単体テスト用関数."""
    # 任意の処理
    return {}


class BookSearchTest(unittest.TestCase):
    """単体テストクラス."""

    # book_search のテストコード
    def test_book_search(self) -> None:
        """`book_search` 関数のテスト."""
        self.assertEqual({}, book_search())


if __name__ == "__main__":
    unittest.main()
