"""キーワードのみ引数."""
from typing import Optional


def increment(page_num: int, last: int, *, ignore_error: bool = False) -> Optional[int]:
    next_page = page_num + 1

    if next_page <= last:
        return next_page

    if ignore_error:
        return None

    raise ValueError("Invalid argument")


def main() -> None:
    print(increment(2, 2, ignore_error=True))
    # 位置引数ではエラーとなる
    # increment(2, 2, True)


if __name__ == "__main__":
    main()
