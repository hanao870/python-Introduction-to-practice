"""モックオブジェクト Mock の動作確認."""
from unittest.mock import Mock


def mock_demo() -> None:
    """モックオブジェクトの動作確認."""
    # 引数で戻り値を設定
    mock = Mock(return_value=3)
    print(f"{mock()=}")

    # return_value は後から変更可能
    mock.return_value = 4
    # 呼び出し時の引数は戻り値に影響しない
    print(f"{mock(1)=}")


def side_effect() -> None:
    """モックオブジェクトの `side_effect` 動作確認."""
    mock = Mock(side_effect=lambda x: x % 2)
    # 関数の場合は引数がそのまま渡される
    print(f"{mock(3)=}")
    # 引数を渡さないとエラーとなる
    # print(f"{mock()=}")

    # イテラブルの場合は呼び出し毎に前から順に返される
    mock.side_effect = [1, 2]
    print(f"{mock()=}")
    print(f"{mock()=}")
    # イテラブルの末尾で呼び出すと StopIteration が送出されエラーとなる
    # print(f"{mock()=}")

    # 例外クラスやそのインスタンスの場合はその例外が送出される
    mock.side_effect = ValueError("エラーです")
    print(f"{mock()=}")


if __name__ == "__main__":
    mock_demo()
    side_effect()
