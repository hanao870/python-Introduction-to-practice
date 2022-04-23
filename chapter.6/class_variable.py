"""
クラス変数の動作確認.

C++ / C# の static 変数
"""


class Page:
    """クラス変数のサンプルクラス."""

    book_title = "Welcome to class variable!"


def main() -> None:
    """メイン関数."""
    print(Page.book_title)

    Page.book_title = "No title"
    print(f"Page.book_title = {Page.book_title}")

    first_page = Page()
    second_page = Page()

    print("----------------------------------------------------------")

    Page.book_title = "Python Practice Book."
    print(f"Page.book_title = {Page.book_title}")
    print(f"first_page.book_title = {first_page.book_title}")
    print(f"secont_page.book_title = {second_page.book_title}")

    print("----------------------------------------------------------")

    first_page.book_title = "[Draft]Python Practice Book."
    print(f"Page.book_title = {Page.book_title}")
    print(f"first_page.book_title = {first_page.book_title}")
    print(f"secont_page.book_title = {second_page.book_title}")


if __name__ == "__main__":
    main()
