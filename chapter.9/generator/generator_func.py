"""ジェネレータ関数の動作確認モジュール."""
from typing import Generator


def gen_function(n: int) -> Generator[int, int, int]:
    """ジェネレータ関数."""
    print("start")
    while n:
        print(f"yield {n}")
        yield n  # ここで一時中断
        n -= 1
    return n  # 関数を抜けると、例外 StopIteration が送出される


def generator_function_test() -> None:
    """ジェネレータ関数の動作確認その1."""
    # ジェネレータイテレータの取得
    g = gen_function(5)
    print(g)

    for i in range(6):
        try:
            # next() に渡すと __next__() が呼ばれる
            print(next(g))  # next(g) の戻り値を表示
            print("--------------")
        except StopIteration:
            print("Then end of g!!")


def gen_fun_test() -> None:
    """ジェネレータ関数の動作確認その2."""
    # for 文での使用
    print("---------- start for ----------")
    for i in gen_function(5):
        print(i)
    print("---------- end for ----------")

    # 内包表記での使用
    print([i for i in gen_function(5)])

    # イテラブルを受け取る関数に渡す
    print(max(gen_function(8)))


if __name__ == "__main__":
    generator_function_test()
    print("---------------------------------")
    gen_fun_test()
