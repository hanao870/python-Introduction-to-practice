"""特殊メソッド __len__ の動作確認."""


class A:
    """特殊メソッド __len__ の動作確認用クラス."""

    def __len__(self) -> int:
        """特殊メソッド `__len__` の動作確認.

        組込み関数 len の引数で渡された時に呼ばれる

        Returns:
            int: 0 以上の長さ
        """
        return 9
        # 0 未満の値を返すとエラーとなる
        # return -1


if __name__ == "__main__":
    print(len(A()))
