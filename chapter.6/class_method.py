"""クラスメソッドの動作確認."""
from operator import attrgetter
from typing import Type, TypeVar

# Klass 型の型変数 T を宣言
T = TypeVar("T", bound="Page")


class Page:
    """クラスメソッドのサンプルクラス."""

    book_title = "Python Practice Book"

    def __init__(self, num: int, content: str) -> None:
        """イニシャライザ."""
        self.num = num
        self.content = content

    def output(self) -> str:
        """コンテンツ出力."""
        return self.content

    # クラスメソッドの第1引数はクラスオブジェクト
    @classmethod
    def print_pages(cls: Type[T], *pages: "Page") -> None:
        """
        各ページの内容をページの昇順に表示.

        第1引数の型アノテーションを以下にするとエラーとなる

        def print_pages(cls: "Page", ...)
        """
        # クラスオブジェクトの利用
        print(f"cls.book_title = {cls.book_title}")

        # ページ順に並び変えて出力
        page_list = list(pages)
        for page in sorted(page_list, key=attrgetter("num")):
            print(f"{page=}")
            print(f"{page.output()}")


def main() -> None:
    """メイン関数."""
    first = Page(1, "first page")
    second = Page(2, "second page")
    third = Page(3, "third page")

    Page.print_pages(first, second, third)

    print("-----------------------------------------------")

    first.print_pages(third, first, second)


if __name__ == "__main__":
    main()
