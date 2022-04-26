"""特殊メソッド __str__ と __repr__ の動作確認."""


class Point:
    """特殊メソッド __str__ と __repr__ の動作確認用クラス."""

    def __init__(self, x: int, y: int) -> None:
        """...

        Args:
            x (int): x 座標
            y (int): y 座標
        """
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """...

        repr() で呼び出される. デバッグ等の情報提供で利用される?

        オブジェクトを再現する為に有効な Python 式がよい(?)

        => 元のオブジェクトに戻せる文字列を返す
        """
        return f"Point({self.x}, {self.y})"

    def __str__(self) -> str:
        """...

        str(), format(), print() 等で呼び出される.

        エンドユーザに出力する為に使用.
        """
        return f"{self.x}, {self.y}"


if __name__ == "__main__":
    p = Point(1, 2)
    # __repr__ 呼び出し
    print(repr(p))
    # __str__ 呼び出し
    print(f"p = {p}")
