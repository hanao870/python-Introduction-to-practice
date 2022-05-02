"""マルチプロセスでのフィボナッチ数列の計算."""
import sys


def fibonacci(n: int) -> int:
    """フィボナッチ数列の計算.

    Args:
        n (int): フィボナッチ数列を計算する番号

    Returns:
        int: `0` から `n+1` 番目のフィボナッチ数列の値
    """
    a = 0
    b = 1

    for _ in range(n):
        a, b = b, b + a
    else:
        return a


def main() -> None:
    """メイン関数."""
    n = int(sys.argv[1])
    print(fibonacci(n))


if __name__ == "__main__":
    main()
