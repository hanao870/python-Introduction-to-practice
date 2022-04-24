"""ローカルスコープの動作確認."""


def f(x: str) -> None:
    """ローカルスコープ表示用."""
    print(f"locals() = {locals()}")

    value = "book"
    print(f"locals() = {locals()}")


if __name__ == "__main__":
    f("hello")
    print(locals())
