"""クロージャの動作確認."""


from typing import Callable


# Callable は呼び出し可能オブジェクトを判定する組込み関数
def counter() -> Callable[[], int]:
    """クロージャの動作確認用関数."""
    count = 0

    def _increment() -> int:
        nonlocal count
        count += 1
        return count

    return _increment


if __name__ == "__main__":
    counter_1 = counter()
    print(f"{counter_1=}")

    print(f"counter_1 = {counter_1()}")
    print(f"counter_1 = {counter_1()}")
    print(f"counter_1 = {counter_1()}")
    print(f"counter_1 = {counter_1()}")
