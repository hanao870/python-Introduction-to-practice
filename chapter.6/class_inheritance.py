"""クラス継承の動作確認."""


class Page:
    """基底クラス."""

    def __init__(self, num: int, content: str) -> None:
        """基底クラスのイニシャライザ."""
        print("call Page initializer.")
        self.num = num
        self.content = content

    def output(self) -> str:
        """コンテンツの出力."""
        print("call Page output method.")
        return self.content


class TitlePage(Page):
    """派生クラス."""

    def __init__(self, num: int, content: str) -> None:
        """派生クラスのイニシャライザ."""
        print("call TitlePage initializer")
        super().__init__(num, content)

    def output(self) -> str:
        """基底クラスのオーバーライド."""
        print("call TitlePage output method.")
        # 基底クラスのメソッドは自動では呼ばれないため、明示的に呼び出す
        title = super().output()
        return title.upper()


# class PageProtocol(Protocol):
#     @property
#     def output(self) -> Page:
#         ...


# T = TypeVar("T", bound=Page)


class HTMLPageMixin:
    """Mixin のベースクラス."""

    def to_html(self) -> str:
        """
        HTML を返す.

        本来は以下のような関数を定義したい.
        self の型アノテーションの方法が不明なので、固定の文字列を返している...

        def to_html(self: Page) -> str:

            return f"<html><body>{self.output()}</body></html>"
        """
        return "<html><body>sample</body></html>"


class WebPage(Page, HTMLPageMixin):
    """Mixin クラス."""

    pass


def call_super() -> None:
    """クラス継承の動作確認."""
    title = TitlePage(0, "Python Practice Book")
    print(f"{title=}")
    print(title.output())

    print("------------------------------------------")

    page = Page(1, "aaa")
    print(f"{page=}")

    page = TitlePage(2, "bbb")

    print(f"{page=}")
    print(page.output())


def call_mixin() -> None:
    """Mixin の動作確認."""
    page = WebPage(0, "web content")
    print(page.to_html())


def main() -> None:
    """メイン関数."""
    call_super()
    call_mixin()


if __name__ == "__main__":
    main()
