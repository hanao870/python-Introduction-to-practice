"""コンテキストマネージャのインスタンス変数の動作確認."""
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


class Point:
    """コンテキストマネージャのインスタンス変数の動作確認クラス."""

    # キーワード引数の型は int のみ
    def __init__(self, **kwargs: int) -> None:
        """イニシャライザ."""
        self.value = kwargs

    @name_deco
    def __enter__(self) -> dict[str, int]:
        """前処理.

        Returns:
            dict[str, int]: キーワード引数のペア
        """
        return self.value  # as 節で渡される

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
        print(self.value)


if __name__ == "__main__":
    with Point(x=12, y=35) as p:
        print(p)
        # __exit__ に直接値を渡す方法がないため
        # インスタンス変数を介して渡す
        p["z"] = 1
