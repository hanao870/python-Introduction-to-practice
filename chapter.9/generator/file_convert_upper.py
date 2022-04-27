"""ジェネレータを用いたファイル変換モジュール."""
import os
from pathlib import Path
from typing import Iterable


def reader(src: str) -> Iterable[str]:
    """ファイルの中身を1行ずつ読み込む.

    Args:
        src (str): ファイルパス

    Yields:
        Generator[str, None, None]: 読み込んだ内容
    """
    with open(src) as f:
        for line in f:
            yield line


def convert(line: str) -> str:
    """`line` を大文字に変換する.

    Args:
        line (str): 変換する文字列

    Returns:
        str: `line` を大文字に変換した文字列
    """
    return line.upper()


def writer(dest: str, reader: Iterable[str]) -> None:
    """ファイルの読込 -> 大文字変換 -> 書き込みを行う.

    Args:
        dest (str): 書き込むファイルパス
        reader (Iterable[str]): ファイルを1行ずつ読み込むジェネレータ関数
    """
    with open(dest, "w") as f:
        for line in reader:
            f.write(convert(line))


if __name__ == "__main__":

    input_file = os.path.join(Path(__file__).parent, "test_data.txt")
    output_file = os.path.join(Path(__file__).parent, "result.txt")

    writer(output_file, reader(input_file))
