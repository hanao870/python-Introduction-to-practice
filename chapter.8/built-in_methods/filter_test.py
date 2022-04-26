"""組込み関数 filter の動作確認."""

from typing import Any, Tuple

if __name__ == "__main__":
    x = (1, 3, 5, 2, 8, 3.1)
    print(filter(lambda i: i > 3, x))
    print(list(filter(lambda i: i > 3, x)))

    # None を渡すと要素の真理値評価で結果を絞り込む
    y: Tuple[Any, ...] = (1, 0, None, 2, [], "python", "")
    print(list(filter(None, y)))
