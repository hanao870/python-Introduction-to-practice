"""組込み関数 map の動作確認."""


if __name__ == "__main__":
    x = [1, 4, 2, 5, 9]

    print(map(lambda i: i * 10, x))
    print(list(map(lambda i: i * 10, x)))

    key = ["q", "limit", "page"]
    value = ["python", 10, 2, 100]

    # 関数が受け取る引数とオブジェクトの数は一致させる
    # イテラブルオブジェクトの数が異なる場合、少ないほうに合わせられる
    print(list(map(lambda k, v: f"{k}={v}", key, value)))

    # join と組み合わせてクエリ文字を作成
    query = "?" + "&".join(map(lambda k, v: f"{k}={v}", key, value))
    print(f"query = {query}")
