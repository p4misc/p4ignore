# p4ignore生成スクリプト

[gibo](https://github.com/simonwhitaker/gibo) と [google/sre_yield](https://github.com/google/sre_yield) を活用して gitignore を p4ignore に変換するスクリプトです。

## 背景
`p4ignore`を使用することで、特定のパターンをもつファイルやディレクトリを、Helix Coreの登録対象外とすることができます。 

参照:
* [環境変数P4IGNORE](https://www.toyo.co.jp/files/user/img/product/ss/help/perforce/r19.1/manuals/cmdref/Content/CmdRef/P4IGNORE.html)
* [p4 ignoresコマンド](https://www.toyo.co.jp/files/user/img/product/ss/help/perforce/r19.1/manuals/cmdref/Content/CmdRef/p4_ignores.html#p4_ignores)
* [P4IGNORE examples](https://community.perforce.com/s/article/6510)

Gitの`gitignore`に相当する機能ですが、`p4ignore`は `\[Aa\]` や `\[0-9\]\*` のようなパターン表記をサポートしていないため、[A collection of .gitignore templates](https://github.com/github/gitignore) をそのまま用いることができません。

パターン表記以外の文法は同等であるため、パターン表記の箇所のみを展開して`p4ignore`に変換するためのごく簡単なスクリプトを作成しました。

## 事前準備

* Python3をインストールします。
* [google/sre_yield](https://github.com/google/sre_yield) モジュールをインストールします。
  ```
  sudo pip3 install sre_yield
  ```
* [gibo](https://github.com/simonwhitaker/gibo) をインストールします。
  ```
  curl -L https://raw.github.com/simonwhitaker/gibo/master/gibo -so ~/bin/gibo && chmod +x ~/bin/gibo && gibo update
  ```

## 使用方法

`gitignore`の内容を **標準入力** または **ファイル指定** で`gitignore_to_p4ignore.py`に与えると、標準出力に変換結果が出力されます。

* 標準入力で与える場合
  ```
  gibo dump UnrealEngine | gitignore_to_p4ignore.py
  ```

* ファイル指定で与える場合

  [UnrealEngine.gitignore](https://github.com/github/gitignore/blob/master/UnrealEngine.gitignore)をダウンロードしていた場合の例:
  ```
  gitignore_to_p4ignore.py UnrealEngine.gitignore
  ```

## 注意事項

### 変換エラーについて
展開されるパターン数が多くなりすぎる場合(20を超える場合)は、標準エラー出力に以下のようなエラーが出力されて変換処理が停止します。
```
ERROR: Too many patterns are generated from the line:
  report.[0-9]*.[0-9]*.[0-9]*.[0-9]*.json
```

この場合は、`\[0-9\]\*` を、単純に `*` に変更するなどした後で再度変換を実行してください。この場合、より広いパターンを網羅することになるため、支障を来たさないかを確認して変更してください。

### 網羅度について
2020年5月17日現在で [A collection of .gitignore templates](https://github.com/github/gitignore) に登録されているすべての`gitignore`のうち、以下の3ファイルを除いてエラーなく変換できることを確認しました。
* Node.gitignore
* TeX.gitignore
* VisualStudio.gitignore

これらのファイルについては、展開されるパターン数が多くなりすぎるため、上記「変換エラーについて」を参考にしてパターンを減少させてください。

※ 具体的な変更例は後日追記します。
