"""コンテキストマネージャ as の動作確認."""
from types import TracebackType
from typing import Optional, ParamSpec, Type, TypeVar

P = ParamSpec("P")  # 引数仕様変数を定義
R = TypeVar("R")  # こちらは通常の型変数


class ContextManager:
    """コンテキストマネージャクラスの動作確認クラス."""

    def __enter__(self) -> int:
        """前処理の実装.

        Returns:
            int: with ブロックに渡す値
        """
        return 1

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[Type[BaseException]],
        traceback: Optional[Type[TracebackType]],
    ) -> None:
        """後処理の実装.

        Args:
            exc_type (Optional[Type[BaseException]]): Exception クラス
            exc_value (Optional[Type[BaseException]]): Exception インスタンス
            traceback (Optional[Type[TracebackType]]): Traceback オブジェクト
        """
        pass


if __name__ == "__main__":
    # __enter__ が何も返さない場合は None となる
    with ContextManager() as f:
        print(f)

    # as の省略
    with ContextManager():
        pass
