"""セイウチ演算子テスト."""
import random
from typing import Optional


def lottery(goods: list[Optional[str]]) -> str:
    # item への代入が行われる
    if item := random.choice(goods):
        return str(item)
    else:
        return "MISS!"


def main() -> None:
    books = ["notebook", "sketchbook", None, None, None]
    print(lottery(books))


if __name__ == "__main__":
    main()
