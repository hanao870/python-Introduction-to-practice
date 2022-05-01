"""デスクリプタの実例."""
from typing import Callable, Generic, ParamSpec, Type, TypeVar, Union

P = ParamSpec("P")  # 引数仕様変数を定義. 引数ありのクラス関数を利用可能にしたかった...
R = TypeVar("R")  # こちらは通常の型変数
T = TypeVar("T")  # 非データデスクリプタを使用するクラス


class LazyProperty(Generic[T]):
    """デコレータとして使用する非データデスクリプタによるキャッシュ.

    クラス関数からの使用を想定
    """

    def __init__(self, func: Callable[[T], R]) -> None:
        """イニシャライザ.

        Args:
            func (Callable[[T], R]): 呼び出し元関数オブジェクト
              引数なしのクラス関数限定
        """
        self.func = func
        self.name = func.__name__
        print(f"{self.func=}, {self.name=}")

    def __get__(self, instance: T, owner: Type[T]) -> Union["LazyProperty[T]", R]:
        """...

        Args:
            instance (T): 呼び出し元クラスのインスタンス.
              型指定で `Optional[T]` とすればクラスオブジェクトからのアクセスを許可する.

              `Optional[T]` の型指定はほぼ意味ないよね?

        Returns:
            _type_: `self.func` の戻り値
        """
        print(f"{instance=}, {owner=}")

        if not instance:
            # クラス変数としてアクセスされた時の処理
            return self
        # self.func は関数なので明示的にクラスのインスタンスを渡す
        v = self.func(instance)
        instance.__dict__[self.name] = v
        return v


TAX_RATE = 1.10


class Book:
    """非データデスクリプタによるキャッシュの使用例."""

    def __init__(self, raw_price: int) -> None:
        """イニシャライザ.

        Args:
            raw_price (int): 本の価格
        """
        print("call Book __init__")
        self.raw_price = raw_price

    @LazyProperty
    def price(self) -> int:
        """税込価格を計算する.

        Returns:
            int: 税込価格(小数点以下切り捨て?)
        """
        print("calculate the price...")
        return int(self.raw_price * TAX_RATE)


if __name__ == "__main__":
    book = Book(1980)
    print(f"{book.price=}")
    # 再度呼ばれた時はキャッシュを使用する
    print(f"{book.price=}")

    # クラスオブジェクトからデスクリプタにアクセスすると None が渡される
    # 型指定で Optional としていないため、mypy でエラーとなる
    # print(Book.price)
