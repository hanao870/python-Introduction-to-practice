"""ひし形継承の動作確認."""


class A:
    """基底クラス."""

    def hello(self) -> None:
        """サンプル関数."""
        print("call class A Hello : Hello!!!")


class B(A):
    """派生クラス その1."""

    def hello(self) -> None:
        """
        サンプル関数.

        基底クラスと同名の関数
        """
        print("call class B Hello : ニーハオ!")
        super().hello()


class C(A):
    """派生クラス その2."""

    def hello(self) -> None:
        """
        サンプル関数.

        基底クラスと同名の関数
        """
        print("call class C Hello : こんちわ!!!")
        super().hello()


class D(B, C):
    """ひし形継承したクラス."""

    def hello(self) -> None:
        """
        サンプル関数.

        ひし形継承したクラスが基底クラスの関数を読んだ場合の動作確認
        """
        print("call class D Hello : Yeah!!!")
        super().hello()


def main() -> None:
    """メイン関数."""
    d = D()
    d.hello()

    print("--------------------------------------------")

    # メソッド解決順序(Method Resolution Order)を確認
    print("Print Method Resolution Order by class D")
    print(D.__mro__)


if __name__ == "__main__":
    main()
