"""マルチプロセスの pickle 化エラーの動作確認."""
from concurrent.futures import ProcessPoolExecutor, wait


def main() -> None:
    """ラムダ式のマルチプロセス(エラーとなる).

    `ProcessPoolExecutor` は `multiprocessing.Queue`
    を用いてプロセス間のデータをやり取りしている.

    `multiprocessing.Queue` は pickle と呼ばれるオブジェクトで
    シリアライズされている.

    以上から、`ProcessPoolExecutor` を使用したマルチプロセス処理では
    pickle 化できないオブジェクトは使用できない.

    pickle 化に関する詳細は以下の URL を参照

    https://docs.python.org/ja/3/library/pickle.html#what-can-be-pickled-and-unpickled
    """
    with ProcessPoolExecutor() as e:
        # ラムダ式は pickle 化できないのでエラーとなる
        future = e.submit(lambda: 1)
        done, not_done = wait([future])

    print(future.result())


if __name__ == "__main__":
    main()
