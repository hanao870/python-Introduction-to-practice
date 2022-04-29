"""デコレータ wraps の動作確認モジュール."""
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def deco4(f: Callable[P, R]) -> Callable[P, R]:
    """標準ライブラリ wraps の動作確認用.

    Args:
        f (Callable[P, R]): 呼び出し元関数オブジェクト
          `P` は呼び出し元関数の引数.
          `R` は呼び出し元関数の戻り値.

    Returns:
        Callable[P, R]: 呼び出し元関数オブジェクト
    """

    @wraps(f)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print("before exec")
        v = f(*args, **kwargs)
        print("after exec")

        return v

    return wrapper


@deco4
def func() -> None:
    """Func ですよ."""
    print("exec func...")


if __name__ == "__main__":
    print(f"func.__name__ = {func.__name__}")
    print(f"func.__doc__ = {func.__doc__}")
