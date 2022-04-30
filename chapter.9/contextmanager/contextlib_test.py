"""標準ライブラリ contextlib.contextmanager の動作確認."""
from contextlib import contextmanager
from typing import Iterator


@contextmanager
def point(**kwargs: int) -> Iterator[dict[str, int]]:
    """デコレータ contextmanager の動作確認クラス.

    Yields:
        Iterator[dict[str, int]]: キーワード引数のイテレータ
    """
    print("__enter__ was called.")
    value = kwargs

    try:
        # yield 式より上が前処理
        # value が as キーワードで渡される
        yield value
        # yield 式より下が後処理
    except Exception as err:
        # エラー時はこちらも呼ばれる
        print(err)
        raise
    finally:
        print("__exit__ was called.")
        print(value)


if __name__ == "__main__":
    with point(x=2, y=5) as p:
        print(p)
        p["z"] = 10
