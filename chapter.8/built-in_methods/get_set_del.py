"""組み込み関数 getattr/setattr/delattr の動作確認."""


class Mutable:
    """組み込み関数 getattr/setattr/delattr の動作確認用クラス."""

    def __init__(self, attr_map: dict[str, int]) -> None:
        """イニシャライザ."""
        # 辞書のキーを属性名にしたインスタンス変数を用意
        for k, v in attr_map.items():
            setattr(self, k, v)


if __name__ == "__main__":
    m = Mutable({"a": 1, "b": 2})
    # mypy では以下はエラーとなる(a の属性を持っていない)
    # print(m.a)
    print(f"getattr(m, 'a') = {getattr(m, 'a')}")

    attr = "b"
    print(f"getattr(m, attr) = {getattr(m, attr)}")

    delattr(m, "a")
    # 属性を削除したのでエラーとなる
    # print(f"getattr(m, 'a') = {getattr(m, 'a')}")

    text = "python"
    # メソッドの取得
    instance_method = getattr(text, "upper")

    print(f"{instance_method=}")
    # text.upper() と同等
    print(f"instance_method() = {instance_method()}")
