"""セイウチ演算子テスト."""


import random


def lottery(goods: list) -> str:
    # item への代入が行われる
    if item := random.choice(goods):
        return item
    else:
        return "MISS!"


def main():
    books = ["notebook", "sketchbook", None, None, None]
    print(lottery(books))


if __name__ == "__main__":
    main()
