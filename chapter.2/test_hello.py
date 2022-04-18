"""unit test demo."""

import unittest


class TestFunc(unittest.TestCase):
    def test_func(self):
        from hello import func
        self.assertIsNone(func("こんちわ"))
