"""グローバルスコープの動作確認."""


def f() -> None:
    """グローバルスコープ変数の表示."""
    # グローバル変数を書き換える場合は
    # global 文で宣言する必要がある
    global x

    print("---------------")
    print("call f function")
    print(f"x = {x}")

    # グローバル変数を先に参照すると
    # 同名の変数は定義できない
    # global x がないと、上の print(x) でエラーとなる
    # x = "f function"
    # print(x)

    x = "book"
    print(f"x = {x}")

    # コンテナオブジェクトのグローバル変数は
    # 先頭の globa y は不要
    y[0] = 100
    print(f"y = {y}")


def g() -> None:
    """グローバルスコープと同名の変数を使用した動作確認."""
    x = "g_function"
    print("---------------")
    print("call g function")
    print(f"x = {x}")


if __name__ == "__main__":
    x = "python"  # モジュール内のグローバルスコープ変数
    y = [x for x in range(10)]  # コンテナオブジェクトのグローバル変数

    print(f"x = {x}")
    print(f"y = {y}")

    f()
    g()

    print("---------------")
    print(f"x = {x}")
    print(f"y = {y}")
