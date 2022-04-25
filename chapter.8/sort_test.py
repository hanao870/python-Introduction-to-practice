"""組込み関数 sort と sorted の動作確認."""

if __name__ == "__main__":
    x = [1, 3, 5, 2, 3, 6]
    y = [1, 3, 5, 2, 3, 6]

    print(f"x = {x}")

    # sort は自身を並び替える
    x.sort()
    print(f"x.sort() = {x}")

    print("--------------------------------------")

    # sorted は新しいリストを返す
    print(f"y = {y}")
    print(f"sorted(y) = {sorted(y)}")
    print(f"y = {y}")
    print(f"sorted(y, reverse=True) = {sorted(y, reverse=True)}")
    print(f"y = {y}")

    print("--------------------------------------")

    z = ["1", "4", 3, 6, 1, "1"]
    # sort/sorted は要素同士が直接比較されるため、異なる型の場合はエラーとなる
    # print(z.sort(reverse=True))
    # print(sorted(z))

    # 比較が等しい場合は元の順序が保持される
    print(f"z = {z}")
    print(sorted(z, key=lambda v: int(str(v))))
