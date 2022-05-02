"""逐次処理とマルチスレッドの比較."""

import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from hashlib import md5
from pathlib import Path
from typing import Callable, ParamSpec, TypeVar
from urllib import request

URL_LIST = ["https://twitter.com", "https://facebook.com", "https://instagram.com"]

P = ParamSpec("P")  # パラメータ仕様変数. パラメータを表す型ヒント
R = TypeVar("R")  # 戻り値の型を R と定義


def elapsed_time(f: Callable[P, R]) -> Callable[P, R]:
    """処理時間を計測するデコレータ.

    Args:
        f (Callable[P, R]): 呼び出し元関数オブジェクト

    Returns:
        Callable[P, R]: 呼び出し元関数オブジェクト
    """

    def inner(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.time()
        v = f(*args, **kwargs)
        print(f"{f.__name__}: {time.time() - start} sec")
        return v

    return inner


def download(url: str) -> tuple[str, str]:
    """`url` で指定されたページをダウンロードする.

    Args:
        url (str): ダウンロードする URL

    Returns:
        tuple[str, str]: 指定した `url` とダウンロードしたファイルパス
    """
    req = request.Request(url)
    # ファイル名に / などが含まれないようにする
    name = md5(url.encode("utf-8"), usedforsecurity=False).hexdigest()

    file_path = Path(__file__).parent.joinpath("download", name)
    with request.urlopen(req) as res:
        Path(file_path).write_bytes(res.read())
        return url, str(file_path)


@elapsed_time
def get_sequential() -> None:
    """`URL_LIST` の URL からページをダウンロードする(逐次処理)."""
    for url in URL_LIST:
        print(f'[{datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f")}] {download(url)}')


@elapsed_time
def get_multi_thread() -> None:
    """`URL_LIST` の URL からページをダウンロードする(マルチスレッド)."""
    # max_workers(最大スレッド数) のデフォルトはコア数×5
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(download, url) for url in URL_LIST]

    for future in as_completed(futures):
        # 完了したものから取得できる
        print(f'[{datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f")}] {future.result()}')


if __name__ == "__main__":
    # 動作確認
    print(download(URL_LIST[0]))

    get_sequential()
    get_multi_thread()
