"""イテラブルオブジェクトの動作確認."""


def zip_test() -> None:
    """組込み関数 zip の動作確認."""
    x = [1, 2, 3]
    y = [4, 5, 6]

    # zip() は複数のイテラブルオブジェクトを受け取り
    # タプルを返すイテレータを作成する組込み関数
    print(f"zip(x, y) = {zip(x, y)}")
    print(f"list(zip(x, y)) = {list(zip(x, y))}")


def zip_each_lenght() -> None:
    """
    組込み関数 zip の動作確認.

    zip に与えるオブジェクトの長さが異なる場合は、
    一番短いオブジェクトの長さになる
    """
    x = [1, 2, 3]
    y = [4, 5, 6, 7]
    z = [8, 9]

    # zip() は一番短いイテレータオブジェクトの長さになる
    print(f"list(zip(x, y, z)) = {list(zip(x, y, z))}")

    from itertools import zip_longest

    # 一番長いオブジェクトに合わせる場合は zip_longest を使用する
    # fillvalue は不足時の値を埋める時に使われる
    print(list(zip_longest(x, y, z, fillvalue=100)))


if __name__ == "__main__":
    zip_test()
    zip_each_lenght()
