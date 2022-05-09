"""unit test demo."""

import unittest


class TestFunc(unittest.TestCase):
    """`import` の動作確認クラス."""

    def test_func(self) -> None:
        """`import` テスト."""
        from .hello import func

        self.assertIsNone(func("こんちわ"))
