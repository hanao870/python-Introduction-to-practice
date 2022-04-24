"""モジュール encoder の動作確認."""

import sys

from b64 import decoder, encoder


def main() -> None:
    """メイン関数."""
    # encoder のタイプ確認
    print(f"{encoder=}")
    # encoder モジュールのトップレベルオブジェクトの確認
    print(dir(encoder))
    # encoder の __name__ 確認
    print(f"encoder.__name__ = {encoder.__name__}")

    print("-----------------------------------------------")

    # decoder のタイプ確認
    print(f"{decoder=}")
    # decoder モジュールのトップレベルオブジェクトの確認
    print(dir(decoder))
    # decoder の __name__ 確認
    print(f"decoder.__name__ = {decoder.__name__}")

    print("-----------------------------------------------")

    # メインモジュールとして実行した __name__ 確認
    print(f"__name__ == {__name__}")

    print("-----------------------------------------------")

    # 第1引数の文字列を変換
    if len(sys.argv) < 2:
        print("第1引数を指定してください")
        return

    target = sys.argv[1]

    print(f"'{target}' を base64 でエンコード")
    b64 = encoder.str_to_base64(target)
    print(b64)

    print(f"{str(b64)} を base64 でデコード")
    print(decoder.base64_to_str(b64))


if __name__ == "__main__":
    main()
