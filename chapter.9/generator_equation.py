"""ジェネレータ式の動作確認モジュール."""
from typing import Generator, Iterable


def chain(iterables: Iterable[str]) -> Generator[str, None, None]:
    """複数のイテラブルを連続した1つのイテラブルに変換するジェネレータ.

    標準ライブラリの itertools.chain() と同じ動き

    Args:
        iterables (Iterable[str]): 変換元のイテラブル

    Yields:
        Generator[str, None, None]: 変換する1文字
    """
    for iterable in iterables:
        print(f"iterable = {iterable}")
        for v in iterable:
            print(f"v = {v}")
            yield v


def new_chain(iterables: Iterable[str]) -> Generator[str, None, None]:
    """複数のイテラブルを連続した1つのイテラブルに変換するジェネレータ.

    yield from を用いたサブジェネレータ

    Args:
        iterables (Iterable[str]): 変換元のイテラブル

    Yields:
        Generator[str, None, None]: 変換する1文字
    """
    for iterable in iterables:
        yield from (v for v in iterable)


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]

    # リスト内包表記
    # 全ての要素がメモリ上に展開される
    listcomp = [i**2 for i in x]
    print(f"list: {listcomp}")

    # ジェネレータ式
    # 各要素は必要になるまで計算されない
    gen = (i**2 for i in x)
    print(gen)

    # リストに展開すると最後の要素まで計算される
    print(f"generator: {list(gen)}")

    # ジェネレータ式が一つだけの場合は () を省略できる
    print(max(i**3 for i in x))

    iterables = ("python", "book")
    print(list(chain(iterables)))
    print(list(new_chain(iterables)))
