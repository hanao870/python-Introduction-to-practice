"""特殊メソッド __contains__ の動作確認モジュール."""


class OddNumber:
    """特殊メソッド __contains__ の動作確認クラス."""

    def __contains__(self, item: int) -> bool:
        """演算子 in で呼ばれる.

        Args:
            item (int): 比較対象の値

        Returns:
            bool: `item` が奇数なら True, 偶数なら False
        """
        return True if item % 2 == 1 else False


if __name__ == "__main__":
    odds = OddNumber()
    print(1 in odds)
    print(4 in odds)
    # 整数のみ対応しているため、float は mypy でエラーとなる
    # print(4.1 in odds)
