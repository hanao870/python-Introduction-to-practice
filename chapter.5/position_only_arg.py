"""位置のみ引数の動作例."""


def add(x: int, y: int, /, z: int) -> int:
    """位置のみ引数としたい引数のあとに / を指定する.

    x と y はキーワード指定できない
    """
    return x + y + z


def main() -> None:
    print(add(2, 3, 4))
    print(add(5, 6, z=7))
    # x と y はキーワード指定できない
    # add(x=10, y=20, z=30)


if __name__ == "__main__":
    main()
