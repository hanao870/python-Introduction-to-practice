"""特殊メソッド __bool__ の動作確認."""


class QueryParams:
    """特殊メソッド __bool__ の動作確認用クラス."""

    def __init__(self, param: dict[str, str]) -> None:
        """...

        Args:
            param (Optional[dict[str, str]]): 辞書
        """
        self.params = param

    # def __bool__(self) -> bool:
    #     """..."""
    #     print("call __bool__")
    #     return bool(self.params)

    def __len__(self) -> int:
        """...

        __bool__ が未定義かつ __len__ が定義済みの場合、bool() で __len__ が呼ばれる.

        __bool__ と __len__ の両方が定義された場合、bool() で __bool__ が呼ばれる.
        """
        print("call __len__")
        return len(self.params)


if __name__ == "__main__":
    query = QueryParams({})
    print(f"bool(query) = {bool(query)}")
    print(f"len(query) = {len(query)}")

    print("----------------------------------")

    query = QueryParams({"key": "value"})
    print(f"bool(query) = {bool(query)}")
    print(f"len(query) = {len(query)}")
