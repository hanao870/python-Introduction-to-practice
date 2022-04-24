"""Base64 形式のバイナリデータを文字列に変換する."""
import base64


def base64_to_str(x: bytes) -> str:
    """Base64 表現を文字列に変換する."""
    return base64.b64decode(x).decode("utf-8")
