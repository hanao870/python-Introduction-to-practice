"""
クラスプロパティの実行例.

C# でいう get / set
"""


class Book:
    """
    プロパティのサンプルクラス.

    Getter / Setter の動作確認
    """

    def __init__(self, raw_price: int) -> None:
        """イニシャライザ."""
        if raw_price < 0:
            raise ValueError("1以上の値段を設定してください")

        self.raw_price = raw_price
        self._discounts: int = 0

    @property
    def discounts(self) -> int:
        """
        クラス変数 discounts の getter.

        @property を最初に記述する必要あり!

        以下の getter / setter の定義はエラーとなる
        @discounts.setter
        def discounts(self, value: int) -> int:
            ...

        @property
        def discounts(self) -> int:
            ...
        """
        print("call discount getter.")
        return self._discounts

    @discounts.setter
    def discounts(self, value: int) -> None:
        """クラス変数 discounts の setter."""
        print("call discount setter.")

        if value < 0 or value > 100:
            raise ValueError("割引率は 0 ~ 100 で設定してください")

        self._discounts = value

    @property
    def price(self) -> int:
        """割引価格."""
        print("call price getter.")
        multi = 100 - self._discounts
        return int(self.raw_price * multi / 100)


def main() -> None:
    """メイン関数."""
    book = Book(2000)
    print(f"discount = {book.discounts}")
    print(f"price = {book.price}")

    print("-------------------------------------")

    book.discounts = 20
    print(f"price = {book.price}")

    print("-------------------------------------")

    try:
        book.discounts = 120
    except ValueError as err:
        print(err)


if __name__ == "__main__":
    main()
