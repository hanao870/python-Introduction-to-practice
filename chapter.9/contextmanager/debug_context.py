"""コンテキストマネージャを用いた一時的なログレベルの変更."""
import logging
from contextlib import contextmanager
from typing import Iterator

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

# デフォルトのログレベルを INFO として DEBUG レベルは無視
logger.setLevel(logging.INFO)


@contextmanager
def debug_context() -> Iterator[None]:
    """デバッグログを一時的に変更するコンテキストマネージャ.

    Yields:
        Iterator[None]: ログレベルを固定する為の空のイテレータ
    """
    level = logger.level

    try:
        # ログレベル変更
        logger.setLevel(logging.DEBUG)
        yield None
    finally:
        # 元のログレベルに戻す
        logger.setLevel(level)


def main() -> None:
    """メイン."""
    logger.info("before info log")
    logger.debug("before debug log")

    # with ブロック内で見たいログの処理を実行する
    with debug_context() as f:
        print(f"{f=}")
        logger.info("inside the block info log")
        logger.debug("inside the block debug log")

    logger.info("after info log")
    logger.debug("after debug log")


if __name__ == "__main__":
    main()
