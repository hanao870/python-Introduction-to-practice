"""サンプルモジュール."""
import imghdr
import pathlib
from typing import Any

from .api import get_data, get_json


class Book:
    """AIP レスポンスの VolumeInfo 要素に対応."""

    def __init__(self, item: dict[str, Any]) -> None:
        """イニシャライザ."""
        self.id = item["id"]
        volume_info = item["volumeInfo"]
        self.imageLinks: dict[str, str]

        for k, v in volume_info.items():
            setattr(self, str(k), v)

    def __repr__(self) -> str:
        """オブジェクトの説明.

        Returns:
            str: オブジェクトの説明文
        """
        return str(self.__dict__)

    def save_thumbnails(self, prefix: str) -> list[pathlib.Path]:
        """サムネイル画像を保存する.

        Args:
            prefix (str): サムネイル画像を保存する書籍

        Returns:
            str: 保存先ディレクトリ
        """
        paths = []
        for kind, url in self.imageLinks.items():
            thumbnail = get_data(url)

            # 画像データから拡張子を判定
            ext = imghdr.what(None, h=thumbnail)

            # pathlib は '/' 演算子でパスを追加できる
            base = pathlib.Path(prefix) / f"{self.id}_{kind}"
            filename = base.with_suffix(f".{ext}")
            filename.write_bytes(thumbnail)
            paths.append(filename)

        return paths


def get_books(q: str, **params: str) -> list[Book]:
    """書籍検索を行う.

    Args:
        q (_type_): 検索する書籍のキーワード
    """
    params["q"] = q
    data = get_json(params)

    return [Book(item) for item in data["items"]]
