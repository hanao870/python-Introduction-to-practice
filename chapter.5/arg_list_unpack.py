"""引数リストのアンパック."""


def print_page(one: str, two: str, three: str) -> None:
    """リストのアンパック."""
    print(one)
    print(two)
    print(three)


def print_page_key(content: str, published: str, author: str) -> None:
    print(content)
    print(f"published: {published}")
    print(f"author: {author}")


def unpack_list() -> None:
    """引数リストのアンパックテスト."""
    content = ["my content 1", "my content 2", "my content 3"]
    print_page(*content)

    # リストが引数より多い場合はエラー
    content += ["my content 4"]
    print(f"content = {content}")
    # print_page(*content)

    content.pop(len(content) - 1)
    content.pop(len(content) - 1)
    print(f"content = {content}")
    # リストが引数より少ない場合はエラー
    # print_page(*content)


def unpack_dict() -> None:
    footer: dict[str, str] = {"published": "2019", "author": "rei suyama"}
    print_page_key("my content 1", **footer)

    # 引数にないキーワードが含まれるとエラー
    # footer["date"] = "10/30"
    # print_page_key("my content 2", **footer)

    # キーワードが不足している場合もエラー
    # footer.pop("author")
    # print_page_key("my content 3", **footer)


def main() -> None:
    unpack_list()
    print("--------------------------------")
    unpack_dict()


if __name__ == "__main__":
    main()
