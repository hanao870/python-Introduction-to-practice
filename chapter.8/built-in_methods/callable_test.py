"""組込み関数 callable の動作確認."""


from typing import Any


class Threshold:
    """特殊関数 __call__ の動作確認."""

    def __init__(self, threshold: int) -> None:
        """イニシャライザ."""
        self.threshold = threshold

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """特殊メソッド."""
        print("call __call__ function")

        if len(args) < 0 or not isinstance(args[0], int):
            return False

        return self.threshold < args[0]


if __name__ == "__main__":
    print(callable(isinstance))  # 関数
    print(callable(Exception))  # クラス
    print(callable("".join))  # メソッド

    threshold = Threshold(2)
    print(threshold(3))
    print(callable(threshold))
