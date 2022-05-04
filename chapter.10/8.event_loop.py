"""イベントループの動作確認."""
import asyncio


async def main() -> None:
    """イベントループの動作確認."""
    # 現在実行中のイベントループを取得
    loop = asyncio.get_running_loop()
    print(loop)


if __name__ == "__main__":
    asyncio.run(main())
