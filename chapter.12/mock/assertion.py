"""モックオブジェクトのアサーションメソッド動作確認モジュール."""
from unittest.mock import ANY, Mock


def assertion_demo() -> None:
    """モックオブジェクトのアサーションメソッド動作確認."""
    mock = Mock(return_value=3)
    # まだ1度も呼び出されていないことを確認
    mock.assert_not_called()

    # 一度だけ呼び出されていることを確認
    # まだ一度も呼び出されていないのでエラーとなる
    # mock.assert_called_once()

    # 呼び出し
    print(f"{mock(1, a=4)=}")
    # 呼び出されているのでエラー
    # mock.assert_not_called()

    # 一度だけ呼ばれていることを確認
    mock.assert_called_once()

    # 呼び出され方を確認
    # 呼び出された時の引数と一致していないのでエラーとなる
    # mock.assert_called_once_with(1, a=1)
    # こちらはOK
    mock.assert_called_once_with(1, a=4)

    # 呼び出し回数は確認せず、一部の引数のみを確認
    mock.assert_called_with(1, a=ANY)


if __name__ == "__main__":
    assertion_demo()
