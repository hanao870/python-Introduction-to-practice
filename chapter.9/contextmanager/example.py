"""コンテキストマネージャの動作例.

標準ライブラリ open による動作確認
"""
import os
from functools import wraps
from pathlib import Path
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def deco(f: Callable[P, R]) -> Callable[P, R]:
    """実行関数名を表示するデコレータ.

    Args:
        f (Callable[P, R]): 呼び出し元関数オブジェクト
          `P` は呼び出し元関数の引数.
          `R` は呼び出し元関数の戻り値.

    Returns:
        Callable[P, R]: 呼び出し元関数オブジェクト
    """

    @wraps(f)
    def inner(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"call {f.__name__}")
        return f(*args, **kwargs)

    return inner


@deco
def demo1(file: str) -> None:
    """コンテキストマネージャの動作その1.

    open() 関数を用いた正常動作の実行例

    Args:
        file (str): ファイル名
    """
    # ファイルを書き込みモードでオープン
    with open(file_path, "w") as f:
        # 書き込まれたバイト数を表示
        print(f.write("python"))

    # ファイルが閉じたか確認
    print(f"{f.closed=}")


@deco
def demo2(file: str) -> None:
    """コンテキストマネージャの動作その2.

    open() 関数を用いた異常動作の実行例

    Args:
        file (str): ファイル名
    """
    try:
        # ファイルを書き込みモードでオープン
        with open(file_path, "w") as f:
            # 書き込みモードなので読込はできないので例外発生
            print(f.read())
    except Exception as err:
        print(f"{err=}")

    # ファイルが閉じたか確認
    print(f"{f.closed=}")


@deco
def demo3(file: str) -> None:
    """コンテキストマネージャの動作その3.

    with を使用しない open() 関数の異常動作の実行例.
    `demo2` と同じ動作となる.

    Args:
        file (str): ファイル名
    """
    try:
        f = open(file_path, "w")
        print(f.read())
    except Exception as err:
        print(f"{err=}")
    finally:
        f.close()

    # ファイルが閉じたか確認
    print(f"{f.closed=}")


if __name__ == "__main__":
    current_path = Path(__file__).parent
    file_path = os.path.join(current_path, "example.txt")

    demo1(file_path)

    print("---------------------------------------")

    demo2(file_path)

    print("---------------------------------------")

    demo3(file_path)
