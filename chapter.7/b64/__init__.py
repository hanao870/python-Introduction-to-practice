"""
Base64 のエンコード/でコードを行うパッケージ.

__init__.py に pydocstyle は不要じゃね？と思ったりしたのだが、

以下の URL で __init__.py にパッケージに関する説明を追加する必要あるんじゃね？と言及している

https://github.com/PyCQA/pydocstyle/issues/55
"""

# 各モジュールのメソッドをインポート
# パッケージ名.属性名で参照できる API を用意
from b64.decoder import base64_to_str
from b64.encoder import str_to_base64

# 'from b64 import *' でインポートされるモジュールを記述
__all__ = ["base64_to_str", "str_to_base64"]

# パッケージインポートの動作確認用メッセージ
print(f"init: {__name__}")
