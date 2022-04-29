"""デコレータ lur_cache の動作確認モジュール."""
from functools import lru_cache
from time import perf_counter, sleep


# 呼び出し結果を32回分キャッシュ
@lru_cache(maxsize=32)
def heavy_function(n: int) -> int:
    """lru_cache の動作確認用関数.

    Args:
        n (int): 任意の整数

    Returns:
        int: 固定値 3
    """
    sleep(3)
    return 3


if __name__ == "__main__":
    # 1回目は時間が掛かる
    start_time = perf_counter()
    val = heavy_function(3)
    end_time = perf_counter()
    print(val)
    print(f"process time: {end_time - start_time} ms")

    # 2回目はキャッシュした結果が返る
    start_time = perf_counter()
    val = heavy_function(3)
    end_time = perf_counter()
    print(val)
    print(f"process time: {end_time - start_time} ms")
