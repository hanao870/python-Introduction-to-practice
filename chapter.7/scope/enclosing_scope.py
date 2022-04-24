"""エンクロージングスコープの動作確認."""


def f() -> None:
    """エンクロージングスコープの動作確認用関数."""
    print("call f function")
    x = "python"

    def g() -> None:
        # nonlocal x  # x がローカル変数でないことを宣言
        x = "Java"  # nonlocal 宣言がない場合は関数 g のローカル変数となる
        print("call g function")
        print(f"x = {x}")
        print("end of g function")

    g()

    print(f"x = {x}")
    print("end of f function")


if __name__ == "__main__":
    f()
