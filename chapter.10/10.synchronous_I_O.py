"""同期 I/O のコルーチン化."""
import asyncio
from hashlib import md5
from pathlib import Path
from urllib import request

URL_LIST = ["https://twitter.com", "https://facebook.com", "https://instagram.com"]


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


async def main() -> None:
    """メイン関数."""
    loop = asyncio.get_running_loop()
    futures = [loop.run_in_executor(None, download, url) for url in URL_LIST]

    for result in await asyncio.gather(*futures):
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
