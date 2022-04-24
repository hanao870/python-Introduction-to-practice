"""モジュール encoder の動作確認."""

import sys

import b64.encoder


def main() -> None:
    """メイン関数."""
    # encoder のタイプ確認
    print(f"{b64.encoder=}")
    # encoder モジュールのトップレベルオブジェクトの確認
    print(dir(b64.encoder))
    # encoder の __name__ 確認
    print(f"b64.encoder.__name__ = {b64.encoder.__name__}")

    # メインモジュールとして実行した __name__ 確認
    print(f"__name__ == {__name__}")

    # 第1引数の文字列を変換
    if len(sys.argv) < 2:
        print("第1引数を指定してください")
        return

    target = sys.argv[1]

    print(f"'{target}' を base64 でエンコード")
    print(b64.encoder.str_to_base64(target))


if __name__ == "__main__":
    main()
