"""Base64 形式のバイナリデータに変換する."""

import base64


def str_to_base64(x: str) -> bytes:
    """文字列を Base64 表現に変換する."""
    return base64.b64encode(x.encode("utf-8"))
