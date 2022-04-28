"""クラスデコレータ dataclass の動作確認モジュール."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Fruit:
    """クラスデコレータ dataclass の動作確認クラス."""

    name: str  # 型ヒントをつけて属性を定義
    price: int = 0  # 初期値 0 を指定


if __name__ == "__main__":
    # __init__ や __repr__ が自動的に追加されている
    apple = Fruit(name="apple", price=125)
    print(repr(apple))

    # frozen=True で読み取り専用のため、値の変更はエラーとなる
    # apple.price = 125
