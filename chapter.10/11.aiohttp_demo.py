"""ライブラリ aiohttp のデモ."""
import asyncio
from typing import Any

import aiohttp


async def fetch(session: aiohttp.ClientSession, url: str) -> Any:
    """非同期 I/O の HTTP リクエスト.

    Args:
        session (aiohttp.ClientSession): HTTP クライアント
        url (str): リクエスト先 URL

    Returns:
        str: `url` の HTML のテキストデータ
    """
    # コンテキストマネージャの非同期版
    async with session.get(url) as response:
        return await response.text()


async def main() -> None:
    """メイン関数."""
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, "http://python.org")
        print(html)


if __name__ == "__main__":
    asyncio.run(main())
