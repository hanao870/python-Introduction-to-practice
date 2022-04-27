"""特殊メソッド __getitem__ と __setitem__ の動作確認モジュール."""
from collections import defaultdict
from typing import Any, DefaultDict


class CountDict:
    """特殊メソッド __getitem__ と __setitem__ の動作確認クラス."""

    def __init__(self) -> None:
        """イニシャライザ.

        インスタンス変数の確保を行う
        """
        self._data: dict[str, int] = {}
        self._get_count: DefaultDict[str, int] = defaultdict(int)
        self._set_count: DefaultDict[str, int] = defaultdict(int)

    def __getitem__(self, key: str) -> int:
        """...

        Args:
            key (str): キー名

        Returns:
            int: キーに対応した値
        """
        # c["x"] などの参照時に呼ばれる
        self._get_count[key] += 1
        return self._data[key]

    def __setitem__(self, key: str, value: int) -> None:
        """...

        Args:
            key (str): キー名
            value (int): 値
        """
        # c["x"] = 1 など代入時に呼ばれる
        self._set_count[key] += 1
        self._data[key] = value

    @property
    def count(self) -> Any:
        """...

        Returns:
            Any: ...
        """
        return {
            "set": list(self._set_count.items()),
            "get": list(self._get_count.items()),
        }


if __name__ == "__main__":
    c = CountDict()
    c["x"] = 1
    print(c["x"])

    c["x"] = 2
    c["y"] = 3

    print(c.count)
