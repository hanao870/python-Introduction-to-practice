"""unit test サンプル."""

import unittest


def book_search():
    return {}


class BookSearchTest(unittest.TestCase):
    # book_search のテストコード
    def test_book_search(self):
        self.assertEqual({}, book_search())


if __name__ == "__main__":
    unittest.main()
