"""マルチスレッドの問題と解決."""
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, wait


class Counter:
    """マルチスレッドでのカウントアップクラス."""

    def __init__(self) -> None:
        """イニシャライザ."""
        self.count = 0

    def increment(self) -> None:
        """カウンタをインクリメント."""
        self.count += 1


class ThreadSafeCounter:
    """スレッドセーフなカウントアップクラス."""

    # ロックを用意する
    lock = threading.Lock()

    def __init__(self) -> None:
        """イニシャライザ."""
        self.count = 0

    def increment(self) -> None:
        """カウンタをインクリメント."""
        with self.lock:
            # 排他制御したい処理をこのブロック内に記述
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


def count_up_thread_safe(counter: ThreadSafeCounter) -> None:
    """カウンタのインクリメントを行う.

    Args:
        counter (Counter): `Counter` クラスのインスタンス
          `increment()` を呼び出す
    """
    # 1000000 回インクリメントする
    for _ in range(1000000):
        counter.increment()


def non_thread_safe_counter() -> None:
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
    print(f"{sys._getframe().f_code.co_name}: {counter.count=:,}")


def thread_safe_counter() -> None:
    """スレッドセーフなカウントアップ."""
    counter = ThreadSafeCounter()
    threads = 2

    with ThreadPoolExecutor() as e:
        # 2つのスレッドを用意して count_up_thread_safe を呼び出す
        futures = [e.submit(count_up_thread_safe, counter) for _ in range(threads)]
        # 全てのスレッドが終了するまで待機
        done, not_done = wait(futures)

    # 数値をカンマ区切りで表示
    # 期待通りの値(2,000,000)になっている
    print(f"{sys._getframe().f_code.co_name}: {counter.count=:,}")


if __name__ == "__main__":
    non_thread_safe_counter()
    thread_safe_counter()
