"""関数のデフォルト引数の動作の注意点."""

from datetime import datetime
from typing import Optional


def print_page_fixed(content: str, time_stamp: datetime = datetime.now()) -> None:
    """デフォルト引数は関数定義時に1度だけ評価される.

    そのため、関数内でデフォルト引数の値を変更した場合、変更された値がデフォルト値となってしまう

    デフォルト値には可変オブジェクトを使用せずに None を指定するのがよい(?)
    """
    print(f"[{time_stamp}] : {content}")


def print_page_dynamic(content: str, time_stamp: Optional[datetime] = None) -> None:
    if time_stamp is None:
        time_stamp = datetime.now()

    print(f"[{time_stamp}] : {content}")


def main() -> None:
    print_page_fixed("my content 1")
    print_page_fixed("my content 2")
    print("---------------------------------------")
    print_page_dynamic("my content 3")
    print_page_dynamic("my content 4")
    print_page_dynamic("my content 5", datetime.now())


if __name__ == "__main__":
    main()
