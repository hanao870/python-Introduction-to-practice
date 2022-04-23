"""スタティックメソッドの動作確認."""


class Page:
    """スタティックメソッドのサンプルクラス."""

    def __init__(self, num: int, content: str) -> None:
        """イニシャライザ."""
        self.num = num
        self.content = content

    # スタティックメソッド宣言
    @staticmethod
    def check_blank(page: "Page") -> bool:
        """
        スタティックメソッド.

        通常の関数と同じなので、使用用途はほぼない
        """
        return bool(page.content)


def main() -> None:
    """メイン関数."""
    page = Page(1, "")
    print(Page.check_blank(page))


if __name__ == "__main__":
    main()
