"""マルチプロセスでのフィボナッチ数列の計算."""
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")  # パラメータ仕様変数. パラメータを表す型ヒント
R = TypeVar("R")  # 戻り値の型を R と定義


def elapsed_time(f: Callable[P, R]) -> Callable[P, R]:
    """処理時間を計測するデコレータ.

    Args:
        f (Callable[P, R]): 呼び出し元関数オブジェクト

    Returns:
        Callable[P, R]: 呼び出し元関数オブジェクト
    """

    def inner(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.time()
        v = f(*args, **kwargs)
        print(f"{f.__name__}: {time.time() - start} sec")
        return v

    return inner


def fibonacci(n: int) -> int:
    """フィボナッチ数列の計算.

    Args:
        n (int): フィボナッチ数列を計算する番号

    Returns:
        int: `0` から `n+1` 番目のフィボナッチ数列の値
    """
    a = 0
    b = 1

    for _ in range(n):
        a, b = b, b + a
    else:
        return a


@elapsed_time
def get_sequential(nums: list[int]) -> None:
    """逐次処理でフィボナッチ数列を計算する.

    Args:
        nums (list[int]): フィボナッチ数列を計算する値のリスト
    """
    for num in nums:
        print(fibonacci(num))


@elapsed_time
def get_multi_process(nums: list[int]) -> None:
    """マルチプロセスでフィボナッチ数列を計算する.

    Args:
        nums (list[int]): フィボナッチ数列を計算する値のリスト
    """
    with ProcessPoolExecutor() as e:
        futures = [e.submit(fibonacci, num) for num in nums]

        # 処理が終了次第、結果を表示
        for future in as_completed(futures):
            print(future.result())


def main() -> None:
    """メイン関数."""
    n = int(sys.argv[1])
    # 論理コア数を取得
    thread_num = os.cpu_count()

    # 論理コアが存在しない場合(mypy でエラーとなる)
    if thread_num is None:
        thread_num = 3

    nums = [n] * thread_num
    # print(get_sequential(nums))
    get_multi_process(nums)


if __name__ == "__main__":
    main()
