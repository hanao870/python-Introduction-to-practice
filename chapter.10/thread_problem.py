"""マルチスレッドの問題と解決."""
from concurrent.futures import ThreadPoolExecutor, wait


class Counter:
    """マルチスレッドでのカウントアップ用クラス."""

    def __init__(self) -> None:
        """イニシャライザ."""
        self.count = 0

    def increment(self) -> None:
        """カウンタをインクリメント."""
        self.count += 1


def count_up(counter: Counter) -> None:
    """カウンタのインクリメントを行う.

    Args:
        counter (Counter): `Counter` クラスのインスタンス
          `increment()` を呼び出す
    """
    # 1000000 回インクリメントする
    for _ in range(1000000):
        counter.increment()


def non_thread_safe() -> None:
    """スレッドセーフでないカウントアップ."""
    counter = Counter()
    threads = 2

    with ThreadPoolExecutor() as e:
        # 2つのスレッドを用意して count_up を呼び出す
        futures = [e.submit(count_up, counter) for _ in range(threads)]
        # 全てのスレッドが終了するまで待機
        done, not_done = wait(futures)

    # 数値をカンマ区切りで表示
    # 2,000,000 にはなっていない(?)
    # 自分の環境では 2,000,000 が表示された...
    print(f"{counter.count=:,}")


if __name__ == "__main__":
    non_thread_safe()
