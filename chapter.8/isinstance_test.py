"""組み込み関数 isinstance の動作確認."""
from collections import UserDict, abc
from typing import Any


class MyDict(UserDict[str, int]):
    """ユーザ定義の辞書風オブジェクト."""

    pass


def get_value(obj: object, key: str) -> Any:
    """
    組み込み関数 isinstance 動作確認.

    isinstance で抽象基底クラスを利用すると、
    直接的な継承関係ではなく、
    必要なメソッドが実装されているかどうかで判定する

    今回は abc.Mapping を使用
    """
    if not isinstance(obj, abc.Mapping):
        raise ValueError

    return obj[key]


if __name__ == "__main__":
    my_dict = MyDict()
    my_dict["a"] = 1
    my_dict["b"] = 2

    print(get_value(my_dict, "a"))
