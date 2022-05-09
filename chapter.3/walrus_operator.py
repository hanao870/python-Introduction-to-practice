"""セイウチ演算子テスト."""
import random
from typing import Optional


def lottery(goods: list[Optional[str]]) -> str:
    """`goods` からランダムに選択された文字列を返す.

    Args:
        goods (list[Optional[str]]): 選択対象のリスト

    Returns:
        str: `goods` から選択された文字列. `None` の場合は `MISS!` を返す
    """
    # item への代入が行われる
    if item := random.choice(goods):
        return str(item)
    else:
        return "MISS!"


def main() -> None:
    """メイン関数."""
    books = ["notebook", "sketchbook", None, None, None]
    print(lottery(books))


if __name__ == "__main__":
    main()
