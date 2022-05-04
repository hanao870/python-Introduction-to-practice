"""コルーチンの動作確認."""
import asyncio
import random
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")  # パラメータ仕様変数. パラメータを表す型ヒント
R = TypeVar("R")  # 戻り値の型を R と定義


def func_name(f: Callable[P, R]) -> Callable[P, R]:
    """関数実行時に関数名を表示するデコレータ.

    Args:
        f (Callable[P, R]): 呼び出し元関数オブジェクト

    Returns:
        Callable[P, R]: 呼び出し元関数オブジェクト
    """

    def inner(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"start {f.__name__}")
        v = f(*args, **kwargs)
        return v

    return inner


async def call_web_api(url: str) -> str:
    """Web API の処理を行うモック.

    Args:
        url (str): API の URL

    Returns:
        str: API の URL
    """
    # Web API の処理をここではスリープで代用
    print(f"send a request: {url}")
    await asyncio.sleep(random.random())
    print(f"got a response: {url}")
    return url


async def async_download(url: str) -> str:
    """Web API の処理を行う.

    Args:
        url (str): API の URL

    Returns:
        str: API の URL
    """
    response = await call_web_api(url)
    return response


@func_name
def single_coroutine() -> None:
    """単体のコルーチン呼び出し."""
    result = asyncio.run(async_download("https://twitter.com"))
    print(f"result = {result}")


@func_name
async def multi_coroutine() -> tuple[str, ...]:
    """複数のコルーチン呼び出し.

    Returns:
        tuple[str, ...]: Web API の URL リスト
    """
    # 呼び出したコルーチンの順番に結果が格納される
    task = asyncio.gather(
        async_download("https://twitter.com"),
        async_download("https://facebook.com"),
        async_download("https://instagram.com"),
    )

    return await task


if __name__ == "__main__":
    single_coroutine()
    result = asyncio.run(multi_coroutine())
    print(f"result = {result}")
