"""コルーチンの動作確認."""
import asyncio
import random


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


def single_coroutine() -> None:
    """単体のコルーチン呼び出し."""
    result = asyncio.run(async_download("https://twitter.com"))
    print(f"result = {result}")


if __name__ == "__main__":
    single_coroutine()
