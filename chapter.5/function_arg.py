"""関数を引数に取る関数."""
from typing import Callable


def print_page(content: str = "no content") -> None:
    print(content)


def print_title(printer: Callable[[str], None], title: str) -> None:
    print("@@@@@")
    # printer は引数 str を取り何も返さない関数オブジェクト
    printer(title.upper())
    print("@@@@@")


def main() -> None:
    print_title(print_page, "python practice book")
    # 指定した関数アノテーションと異なるオブジェクトではエラー
    # print_title(10, "test")


if __name__ == "__main__":
    main()
