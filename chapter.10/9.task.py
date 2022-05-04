"""タスクの動作確認."""
import asyncio
import time
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


async def coro(n: int) -> int:
    """タスクの動作確認用関数.

    Args:
        n (int): sleep 時間(秒)

    Returns:
        int: sleep 時間(秒)
    """
    await asyncio.sleep(n)
    return n


async def task_demo() -> int:
    """メイン関数."""
    # タスクの作成
    # タスクは、実行がスケジューリングされたコルーチンをカプセル化したもの
    task = asyncio.create_task(coro(1))
    print(task)
    return await task


@elapsed_time
async def use_task() -> None:
    """タスクを使用した複数のコルーチン実行."""
    # 3秒で完了する
    task1 = asyncio.create_task(coro(1))
    task2 = asyncio.create_task(coro(2))
    task3 = asyncio.create_task(coro(3))

    print(await task1)
    print(await task2)
    print(await task3)


@elapsed_time
async def not_task() -> None:
    """タスクを使用せずにコルーチンのまま実行."""
    # 6秒かかる
    print(await coro(1))
    print(await coro(2))
    print(await coro(3))


if __name__ == "__main__":
    asyncio.run(task_demo())
    asyncio.run(use_task())
    asyncio.run(not_task())
