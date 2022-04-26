"""特殊メソッド  の動作確認."""


class Point:
    """特殊メソッド __setattr__ と __delattr__ の動作確認用クラス."""

    def __init__(self, x: int, y: int) -> None:
        """イニシャライザ.

        Args:
            x (int): X 座標
            y (int): Y 座標
        """
        self.x = x
        self.y = y

    def __setattr__(self, __name: str, __value: int) -> None:
        """..."""
        if __name not in ("x", "y"):
            raise AttributeError("Not allowed")

        # 値を設定するには基底クラスの __setattr__ を呼び出す
        super().__setattr__(__name, __value)
        # self で値を代入すると __setattr__ が呼ばれる
        # 無限ループとなり例外 RecursionError が発生する
        # self.x = __value

    def __delattr__(self, __name: str) -> None:
        """..."""
        if __name in ("x", "y"):
            raise AttributeError("Not allowed")

        # self を del すると __delattr__ が呼ばれる
        # del self.x
        super().__delattr__(__name)


if __name__ == "__main__":
    p = Point(1, 2)
    p.x = 9
    print(p.x)

    # 属性 z は存在しないのでエラーとなる
    # p.z = 4

    # 属性 x の削除は許可しないのでエラーとなる
    # del p.x
