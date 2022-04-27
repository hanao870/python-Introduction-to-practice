"""特殊メソッド __iter__ の動作確認モジュール."""
from typing import Iterator


class Iterable:
    """特殊メソッド __iter__ の動作確認クラス."""

    def __init__(self, num: int) -> None:
        """イニシャライザ.

        Args:
            num (int): 整数の幅
        """
        self.num = num
        pass

    def __iter__(self) -> Iterator[int]:
        """...

        Returns:
            Iterable[int]: 組込み関数 range() が返すイテレータ
        """
        return iter(range(self.num))


if __name__ == "__main__":
    print([v for v in Iterable(3)])
