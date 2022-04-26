"""特殊メソッド __call__ の動作確認."""
from typing import Any


class Adder:
    """特殊メソッド __call__ の動作確認用クラス."""

    def __init__(self) -> None:
        """..."""
        self._values: list[int] = []

    def add(self, x: int) -> None:
        """配列末尾に値を追加する.

        Args:
            x (int): 追加する値
        """
        self._values.append(x)

    def __call__(self) -> Any:
        """..."""
        print("call __call__")
        return sum(self._values)


def f() -> int:
    """..."""
    return 1


if __name__ == "__main__":
    adder = Adder()

    adder.add(1)
    adder.add(3)
    print(adder())

    adder.add(0)
    adder.add(25)
    print(adder())

    # 関数オブジェクトは __call__ 属性を持つ
    # 関数オブジェクトの実態は __call__ を実装した function クラスのインスタンスとなっている
    print(dir(f))
