"""デコレータによる処理時間の計測."""
import time
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def elapsed_time(f: Callable[P, R]) -> Callable[P, R]:
    """処理時間を計測するデコレータ.

    Args:
        f (Callable[P, R]): 呼び出し元関数オブジェクト
          `P` は呼び出し元関数の引数.
          `R` は呼び出し元関数の戻り値.

    Returns:
        Callable[P, R]: 呼び出し元関数オブジェクト
    """

    @wraps(f)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.time()
        v = f(*args, **kwargs)
        print(f"elapsed time for {f.__name__}: {time.time() - start} sec")
        return v

    return wrapper


@elapsed_time
def func(n: int) -> int:
    """0 から `n` - 1 までの総和を計算する.

    Args:
        n (int): 計算する値

    Returns:
        int: 0 から `n` - 1 までの総和
    """
    return sum(i for i in range(n))


if __name__ == "__main__":
    # 数値をカンマ区切りで表示
    print(f"{func(100000)=:,}")
    print(f"{func(100000000)=:,}")
