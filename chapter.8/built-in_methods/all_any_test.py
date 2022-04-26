"""組込み関数 all/any の動作確認."""

if __name__ == "__main__":
    x = ["python", "practice", "book"]
    y = {0: "test", 1: ""}
    z = ["", None, 0]

    print(f"x = {x}")
    print(f"y = {y}")
    print(f"z = {z}")

    print("--------------------------------------------------")

    # all はリテラブルオブジェクトの全要素が真の場合に True を返す
    print(f"all(x) = {all(x)}")
    # 辞書の場合はキーで判定される
    print(f"all(y) = {all(y)}")
    print(f"all(z) = {all(z)}")

    print("--------------------------------------------------")

    # any はリテラブルオブジェクトの要素が1つでも真の場合に True を返す
    print(f"any(x) = {any(x)}")
    print(f"any(y) = {any(y)}")
    print(f"any(z) = {any(z)}")
