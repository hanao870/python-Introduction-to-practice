"""データデスクリプタの動作確認."""
from functools import wraps
from typing import Any, Callable, ParamSpec, Type, TypeVar

P = ParamSpec("P")  # 引数仕様変数を定義
R = TypeVar("R")  # こちらは通常の型変数
T = TypeVar("T")


def func_name(f: Callable[P, R]) -> Callable[P, R]:
    """呼び出し元関数名を表示するデコレータ.

    Args:
        f (Callable[P, R]): 呼び出し元関数オブジェクト

    Returns:
        Callable[P, R]: 呼び出し元関数オブジェクト
    """

    @wraps(f)
    def inner(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"{f.__name__} was called")
        return f(*args, **kwargs)

    return inner


# __set__ を持つクラスはデータデスクリプタ
class TextField:
    """データデスクリプタの動作確認クラス."""

    @func_name
    def __set_name__(self, owner: "Book", name: str) -> None:
        """`name` を設定する.

        Args:
            owner (str): オーナー
            name (str): 名前(?)
        """
        print(f"{owner=}, {name=}")
        self.name = name

    @func_name
    def __set__(self, instance: "Book", value: str) -> None:
        """...

        Args:
            instance (Book): デスクリプタを使用しているクラスオブジェクト
            value (str): 設定する値

        Raises:
            AttributeError: `value` が `str` でない
        """
        print(f"{instance=}")

        if not isinstance(value, str):
            raise AttributeError("must be 'str'")

        # ドット表記ではなく属性辞書を使って格納
        instance.__dict__[self.name] = value

    @func_name
    def __get__(self, instance: "Book", owner: Type["Book"]) -> Any:
        """...

        Args:
            instance (Book): デスクリプタを使用しているクラスオブジェクト
            owner (Type["Book"]): ???

        Raises:
            KeyError: `name` キーが存在しない

        Returns:
            Any: `name` の値
        """
        print(f"{instance=}, {owner=}")

        if self.name not in instance.__dict__:
            raise KeyError(f"Value not found in '{self.name}'")

        return instance.__dict__[self.name]


class Book:
    """データデスクリプタを使用するクラス."""

    title = TextField()


if __name__ == "__main__":
    book = Book()

    # 代入時には __set__() が呼ばれる
    book.title = "Python Practice Book"

    # 取得時には __get__() が呼ばれる
    print(f"{book.title=}")

    # 別のインスタンスを作成して代入
    notebook = Book()
    notebook.title = "NoteBook"

    # 各インスタンス毎にデータを保持している
    print(f"{book.title=}")
    print(f"{notebook.title=}")

    # try:
    #     # 文字列以外の代入はエラーとなる(mypy でエラー判定される)
    #     book.title = 123
    # except AttributeError as err:
    #     print(err)
