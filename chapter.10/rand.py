"""マルチプロセスの乱数生成."""
import random
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import Any, Callable, ParamSpec, TypeVar

import numpy

P = ParamSpec("P")  # パラメータ仕様変数. パラメータを表す型ヒント
R = TypeVar("R")  # 戻り値の型を R と定義


def func_name(f: Callable[P, R]) -> Callable[P, R]:
    """関数実行時に関数名を表示するデコレータ.

    Args:
        f (Callable[P, R]): 呼び出し元関数オブジェクト

    Returns:
        Callable[P, R]: 呼び出し元関数オブジェクト
    """

    def inner(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"start {f.__name__}")
        v = f(*args, **kwargs)
        return v

    return inner


def use_numpy_random() -> Any:
    """`numpy` を用いた乱数生成.

    Returns:
        float: 乱数値
    """
    # 乱数生成器を初期化する場合はこの行を実行する
    numpy.random.seed()
    # Linux 環境ではプロセスの開始方式が fork となっているため
    # 乱数生成器を初期化しない場合、同一の乱数となる
    return numpy.random.random()


def use_random() -> float:
    """標準ライブラリの `random` を用いた乱数生成.

    標準ライブラリの `random` はプロセスが fork の際、
    自動で乱数生成器が初期化される

    Returns:
        float: 乱数値
    """
    return random.random()


@func_name
def numpy_random_multi_process() -> None:
    """マルチプロセスで `numpy` の乱数を生成する."""
    with ProcessPoolExecutor() as e:
        futures = [e.submit(use_numpy_random) for _ in range(3)]

        for future in as_completed(futures):
            print(future.result())


@func_name
def standard_random_multi_process() -> None:
    """マルチプロセスで標準ライブラリの random を用いて乱数を生成する."""
    with ProcessPoolExecutor() as e:
        futures = [e.submit(use_random) for _ in range(3)]

        for future in as_completed(futures):
            print(future.result())


def main() -> None:
    """メイン関数."""
    numpy_random_multi_process()
    standard_random_multi_process()


if __name__ == "__main__":
    main()
