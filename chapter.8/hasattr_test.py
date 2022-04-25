"""
組込み関数 hasattr の動作確認.

第1引数のオブジェクトが、第2引数の名前の属性を持っているか判定
"""
import json
import os


def is_package(module_or_package: object) -> bool:
    """
    パッケージオブジェクトの判定.

    パッケージオブジェクトは必ず __path__ を持つ
    """
    return hasattr(module_or_package, "__path__")


if __name__ == "__main__":
    # json モジュールはパッケージ
    print(f"is_package(json) = {is_package(json)}")

    # os モジュールは単体ファイル
    print(f"is_package(os) = {is_package(os)}")
