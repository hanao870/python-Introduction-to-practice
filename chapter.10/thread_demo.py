"""非同期処理のデモ."""

from concurrent.futures import Future, ThreadPoolExecutor


# 非同期に実行する処理
def func() -> int:
    """非同期処理のサンプル.

    Returns:
        int: 終了コード
    """
    for i in range(100000):
        pass

    return 1


if __name__ == "__main__":
    # スケジューリングされた呼び出し可能オブジェクトをカプセル化(?)
    future = ThreadPoolExecutor().submit(func)

    print(f"{isinstance(future, Future)=}")
    print(f"{future.result()=}")
    # 非同期処理の状態を表示
    print(f"{future.done()=}")
    print(f"{future.running()=}")
    print(f"{future.cancelled()=}")
