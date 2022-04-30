"""コンテキストマネージャクラスの動作確認."""
from functools import wraps
from types import TracebackType
from typing import Callable, Optional, ParamSpec, Type, TypeVar

P = ParamSpec("P")  # 引数仕様変数を定義
R = TypeVar("R")  # こちらは通常の型変数


def name_deco(f: Callable[P, R]) -> Callable[P, R]:
    """ログ出力デコレータ.

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


class ContextManager:
    """コンテキストマネージャクラスの動作確認クラス."""

    @name_deco
    def __enter__(self) -> None:
        """前処理の実装."""
        pass

    @name_deco
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[Type[BaseException]],
        traceback: Optional[Type[TracebackType]],
    ) -> None:
        """後処理の実装.

        Args:
            exc_type (Optional[Type[BaseException]]): Exception クラス
            exc_value (Optional[Type[BaseException]]): Exception インスタンス
            traceback (Optional[Type[TracebackType]]): Traceback オブジェクト
        """
        print(f"{exc_type=}")
        print(f"{exc_value=}")
        print(f"{traceback=}")


if __name__ == "__main__":
    # with ブロックが正常終了の場合は
    # __exit__ の引数は全て None
    with ContextManager():
        print("inside the block.")

    # with ブロック内で例外が発生した場合は
    # __exit__ の引数に情報が渡される
    with ContextManager():
        1 / 0
