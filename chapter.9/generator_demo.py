"""ジェネレータの動作デモモジュール."""
from typing import Generator


def inf(n: int) -> Generator[int, int, int]:
    """ジェネレータの動作でも関数."""
    while True:
        yield n


for i in inf(3):
    print(i)
