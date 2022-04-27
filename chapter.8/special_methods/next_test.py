"""独自イテレータの動作確認."""


class Reverse:
    """独自イテレータの動作確認クラス."""

    def __init__(self, x: list[int]) -> None:
        """イニシャライザ.

        Args:
            x (list[int]): 要素
        """
        self.x = x
        pass

    def __iter__(self) -> "Reverse":
        """...

        Returns:
            Reverse: 自身のインスタンスを返す
        """
        print("call __iter__")
        return self

    def __next__(self) -> int:
        """...

        Raises:
            StopIteration: 要素が空でループを終了させる

        Returns:
            int: 要素の値
        """
        print("call __next__")
        try:
            return self.x.pop()
        except IndexError:
            raise StopIteration()


if __name__ == "__main__":
    print([val for val in Reverse([1, 2, 3, 4])])
