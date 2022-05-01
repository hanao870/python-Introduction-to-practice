"""非データデスクリプタの動作確認."""
from functools import wraps
from typing import Any, Callable, ParamSpec, Type, TypeVar

P = ParamSpec("P")  # 引数仕様変数を定義
R = TypeVar("R")  # こちらは通常の型変数


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


# __get__ のみであれば非データデスクリプタ
class TextField:
    """非データデスクリプタの動作確認クラス."""

    @func_name
    def __init__(self, value: str) -> None:
        """イニシャライザ.

        Args:
            value (str): 設定値

        Raises:
            AttributeError: `value` が `str` でない
        """
        if not isinstance(value, str):
            raise AttributeError("must be str")
        self.value = value

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
        return self.value


class Book:
    """非データデスクリプタを使用するクラス."""

    title = TextField("Python Practice Book")


if __name__ == "__main__":
    book = Book()
    print("-----------------------------------")

    # 代入前の取得時には __get__() が呼ばれる
    print(f"{book.title=}")

    # 代入するとインスタンス変数になる
    book.title = "Book"

    print("-----------------------------------")

    # インスタンスがあると __get__ は呼ばれない
    print(f"{book.title=}")

    print("-----------------------------------")

    # 別のインスタンスを作成して代入
    notebook = Book()
    notebook.title = "NoteBook"

    # 各インスタンス毎にデータを保持している
    print(f"{book.title=}")
    print(f"{notebook.title=}")
