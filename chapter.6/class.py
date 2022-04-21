"""クラス動作確認."""
from typing import Optional


class Page:
    def __init__(self, num: int, content: str, section: Optional[int] = None) -> None:
        """インスタンス生成後に呼び出される.

        Python ではコンストラクタではなくイニシャライザと呼ばれる
        """
        self.num = num
        self.content = content
        self.section = section

    def output(self) -> str:
        return f"{self.content}"


def main() -> None:
    title_page = Page(0, "Python Practice Book")
    print(type(title_page))

    # Page クラスのインスタンス確認
    print(isinstance(title_page, Page))

    # インスタンスが持つ属性確認
    print(dir(title_page))

    # インスタンスメソッド呼び出し
    print(title_page.output())

    first_page = Page(1, "first Page", 1)
    print(f"first_page.section = {first_page.section}")


if __name__ == "__main__":
    main()
