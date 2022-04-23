"""可変長引数の動作確認."""


def print_pages_1(content: str, *args: str) -> None:
    """可変長の位置引数."""
    print(content)
    # args の型情報を表示
    print(f"{args=}")
    print(f"type(args) = {type(args)}")

    for more in args:
        print(f"more: {more}")


def print_pages_2(content: str, **kwargs: object) -> None:
    """可変長のキーワード引数."""
    print(content)

    for key, value in kwargs.items():
        print(f"{key}: {value}")


def print_pages_3(*args: str, **kwargs: object) -> None:
    """可変長の位置引数とキーワード引数."""
    for content in args:
        print(content)

    for key, value in kwargs.items():
        print(f"{key}: {value}")


def main() -> None:
    """メイン関数."""
    print_pages_1("My content 1")  # args は空のタプル
    print_pages_1("My content 2", "content2", "content3")

    print("--------------------------------------------")

    print_pages_2("My content 3", published=2019, author="rei suyama")

    print("--------------------------------------------")

    print_pages_3(
        "My content 1",
        "My content 2",
        "My content 3",
        published=2019,
        author="rei suyama",
    )


if __name__ == "__main__":
    main()
