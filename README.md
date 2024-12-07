# robosys2024

ロボットシステム学
・講義用
・課題用

## 四則演算コマンド

### 概要

task_computerは、四則演算（足し算、引き算、掛け算、割り算）をターミナル上で実行できるコマンドです。標準入力から操作と数値を受け取り、計算結果を標準出力に表示します。

# 必要なソフトウェア

・Python（3.7～3.11でテスト済み）

## インストール方法

事前準備

1.Gitをインストールしていない場合、以下のコマンドでインストールしてください。

```
sudo apt install git
```

2.リポジトリをクローンします。

```
git clone https://github.com/skt-0628/robosys2024.git

```

3.ディレクトリを移動し、スクリプトを実行可能にします。

```
cd robosys2024/src
chmod +x computer.py
```

### 実行方法

以下のコマンドで実行します。

```
echo "add 3 4" | ./computer.py
```

結果

```
7.0
```

操作方法ガイド

・add:足し算

・subtract:引き算

・multiply:掛け算

・divide:割り算


エラー例

無効な入力や操作が行われた場合、エラーメッセージが出力されます。


```
echo "divide 5 0" | ./computer.py
エラー: ０で割ることはできません
```

# ライセンス


・このプロジェクトは、３条項BSDライセンスのもとで公開されています。詳しくは [LICENSE](LICENSE) をご覧ください。

・このパッケージのコードの一部は、下記URL(CC-BY-SA 4.0 by Ryuichi Ueda)のを、本人の許可を得て作成しています。
　https://ryuichiueda.github.io/slides_marp/robosys2024/lesson6.html

## 著者

坂田拓海

Email:no4nixs20@gmail.com

GitHub:skt-0628
