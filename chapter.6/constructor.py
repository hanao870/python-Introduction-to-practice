"""コンストラクタとイニシャライザ.

必要なとき以外は __new__() の利用は避けるように!!
"""
from typing import Type, TypeVar

# Klass 型の型変数 T を宣言
T = TypeVar("T", bound="Klass")


class Klass:
    def __new__(cls: Type[T], *args: object) -> T:
        """こちらはコンストラクタ."""
        print(f"{cls=}")
        print(f"new {args}")
        # インスタンスを作成して返す
        return super().__new__(cls)

    def __init__(self, *args: object) -> None:
        """こちらはイニシャライザ."""
        # インスタンスの初期化はこちらで行う
        print(f"init {args}")


def main() -> None:
    Klass(1, 2, 3)


if __name__ == "__main__":
    main()
