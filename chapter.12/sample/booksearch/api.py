"""サンプルモジュール."""
import json
from typing import Any
from urllib import parse, request


def get_json(param: Any) -> Any:
    """Google Books APIs による書籍検索を行う.

    Args:
        param (Any): 検索キーワード

    Returns:
        Any: 検索結果の JSON データ
    """
    with request.urlopen(build_url(param)) as f:
        return json.load(f)


def get_data(url: str) -> Any:
    """`url` で指定したオブジェクトを取得する.

    Args:
        url (str): URL

    Returns:
        Any: `url` で指定したオブジェクト
    """
    with request.urlopen(url) as f:
        return f.read()


def build_url(param: Any) -> str:
    """Google Books APIs の URL を生成する.

    Args:
        param (Any): 検索キーワード

    Returns:
        str: Google Books APIs の URL
    """
    query = parse.urlencode(param)
    return f"https://www.googleapis.com/books/v1/volumes?{query}"
