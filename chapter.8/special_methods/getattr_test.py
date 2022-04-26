"""特殊メソッド __getattr__ と __getattribute__ の動作確認モジュール."""
import json
import os
from pathlib import Path
from typing import Any


class Point:
    """__dict__ と __getattribute__ の動作確認用クラス."""

    pass


class Config:
    """特殊メソッド __getattr__ の動作確認用クラス."""

    def __init__(self, filename: str) -> None:
        """イニシャライザ.

        Args:
            filename (str): json ファイル名
        """
        self.config = json.load(open(filename))

    def __getattr__(self, name: str) -> Any:
        """..."""
        if name in self.config:
            return self.config[name]
        # 存在しない設定値へのアクセスはエラーとする
        raise AttributeError(f"No attribute '{name}'")


def test_getattribute() -> None:
    """__getattribute__ の動作確認."""
    p = Point()
    print(f"p.__dict__ = {p.__dict__}")

    # 以下の代入は mypy で属性無しと判定されてエラーとなる
    # __getattr__ を定義すれば可能?
    # p.x = 1
    p.__dict__["x"] = 1
    print(f"p.__dict__ = {p.__dict__}")
    # 以下の呼び出しは mypy で属性無しと判定されてエラーとなる
    # __getattr__ を定義すれば呼び出し可能となる
    # print(p.x)
    print(p.__getattribute__("x"))

    p.__dict__["y"] = 2
    print(f"p.__dict__ = {p.__dict__}")
    print(p.__getattribute__("y"))


def test_getattr() -> None:
    """__getattr__ の動作確認."""
    config = Config(os.path.join(Path(__file__).parent, "config.json"))
    print(f"config.url = {config.url}")
    print(config.xxx)


if __name__ == "__main__":
    test_getattribute()
    test_getattr()
