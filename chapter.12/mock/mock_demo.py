"""モックオブジェクト Mock の動作確認."""
from unittest.mock import Mock

if __name__ == "__main__":
    # 引数で戻り値を設定
    mock = Mock(return_value=3)
    print(f"{mock()=}")

    # return_value は後から変更可能
    mock.return_value = 4
    # 呼び出し時の引数は戻り値に影響しない
    print(f"{mock(1)=}")
