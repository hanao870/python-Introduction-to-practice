"""関数デコレータの作成."""


# デコレートしたい関数を受け取る
from typing import Callable, Tuple


def deco1(f: Callable[[], int]) -> Callable[[], int]:
    """ログ出力するデコレータ.

    Args:
        f (Callable[[], int]): ログを記録する関数

    Returns:
        Callable[[], int]: `f` の戻り値
    """
    print("deco1 called.")

    def wrapper() -> int:
        print("before exec.")
        v = f()  # 元の関数を実行
        print("after exec.")
        return v

    return wrapper


def deco2(
    f: Callable[[int, int], Tuple[int, int]]
) -> Callable[[int, int], Tuple[int, int]]:
    """引数を受け取るデコレータ.

    Args:
        f (Callable[[int, int], Tuple[int, int]]): 呼び出し元関数

    Returns:
        Callable[[int, int], Tuple[int, int]]: 実行元の関数オブジェクト
    """
    # 新しい関数が引数を受け取る
    def wrapper(*args: int, **kwargs: object) -> Tuple[int, int]:
        print("before exec")
        # 引数を渡して関数を実行
        v = f(*args, **kwargs)
        print("after exec.")
        return v

    return wrapper


def deco3(
    z: int,
) -> Callable[
    [Callable[[int, int], Tuple[int, int]]], Callable[[int, int], Tuple[int, int]]
]:
    """...

    Args:
        z (int): 任意の整数

    Returns:
        Callable[ [Callable[[int, int], Tuple[int, int]]], Callable[[int, int], Tuple[int, int]] ]: そもそもこの定義方法まちがっているのでは？
    """
    print("call deco3")

    def _deco3(
        f: Callable[[int, int], Tuple[int, int]]
    ) -> Callable[[int, int], Tuple[int, int]]:
        print("call _deco3")

        def wrapper(*args: int, **kwargs: object) -> Tuple[int, int]:
            print(f"before exec {z}")
            v = f(*args, **kwargs)
            print(f"after exec {z}")

            return v

        return wrapper

    # デコレータを返す
    return _deco3


@deco1
def func1() -> int:
    """自作デコレータ `deco1` の動作確認用関数.

    Returns:
        int: 固定値 1
    """
    print("exec")
    return 1


@deco2
def func2(x: int, y: int) -> Tuple[int, int]:
    """自作デコレータ `deco2` の動作確認用関数.

    Args:
        x (int): 任意の整数
        y (int): 任意の整数

    Returns:
        Tuple[int, int]: `x` と `y` のタプル (`x`, `y`)
    """
    print("exec")
    return x, y


@deco3(z=3)  # func = deco3(z=3)(func) と同等
@deco3(z=30)
def func3(x: int, y: int) -> Tuple[int, int]:
    """自作デコレータ `deco2` の動作確認用関数.

    Args:
        x (int): 任意の整数
        y (int): 任意の整数

    Returns:
        Tuple[int, int]: `x` と `y` のタプル (`x`, `y`)
    """
    print("exec func3")
    return x, y


if __name__ == "__main__":
    print(f"func1.__name__ = {func1.__name__}")
    print(func1())

    print(f"func2.__name__ = {func2.__name__}")
    print(func2(1, 2))

    print(f"func3.__name__ = {func3.__name__}")
    print(func3(1, 2))
    print(func3(3, 4))

    # func3(1, 2) は print 内の記述と同じ
    # deco3(z=3) -> _deco3 の関数オブジェクトが返る
    # deco3(z=3)(func) => _deco3(func) -> wrapper の関数オブジェクトが返る
    # deco3(z=3)(func3)(1, 2) => _deco3(func)(1, 2) => wrapper(1, 2) -> func(1, 2) の処理結果が返る
    print(deco3(z=3)(func3)(1, 2))
