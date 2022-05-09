# Pytho 開発環境 for Remote Container

以下の書籍のプログラムに `mypy` の型アノテーションを追加下した写経リポジトリ

* [Python実践入門──言語の力を引き出し、開発効率を高める](https://gihyo.jp/book/2020/978-4-297-11111-3)

## 開発環境

以下の開発環境にて Python の動作確認を実施

* Windows 10 pro Version 21H2
* Docker Desktop for Windows
* Python Docker Official Image
  * `python:3.10.4`
* `Visual Studio Code`
  * 拡張機能: `Remote - Container`

`Visual Studio Code` から Python のコンテナにアクセスして開発を行う

以下の `Visual Studio Code` の拡張機能がコンテナ内にインストールされる

* `Python`
* `Pylance`
* `markdownlint`
* `Git history`
* `autoDocstring - Python Docstring Generator`
* `indent-rainbow`

## Python の linter / formatter

以下の linter / formatter を使用

* linter
  * [flake8](https://github.com/PyCQA/flake8)
  * [bandit](https://github.com/PyCQA/bandit)
  * [pydocstyle](https://github.com/PyCQA/pydocstyle)
  * [mypy](https://github.com/python/mypy)
* formatter
  * [black](https://github.com/psf/black)
  * [isort](https://github.com/PyCQA/isort)

Ctrl + S でファイルを保存すると formatter が実行されるよう、コンテナ内の `Visual Studio Code` の設定を変更している
