# robosys2024
#プロジェクトタイトル

四則演算コマンド
このリポジトリには、ターミナル上で四則演算が行えるcomputer.pyがあります。標準入出力を利用し、基本的な計算を行います。

## インストール方法

リポジトリをクローンする
git clone https://gitnub.com/skt-0628/robosys2024

ディレクトリに移動
cd robosys2024

スクリプトに実行権限を与える
chmod +x computer.py

##使い方

1.スクリプトを実行
./computer.py


2.メニューが表示される

___ 四則演算___
1. 足し算（＋）
2. 引き算（－）
3. 掛け算（＊）
4. 割り算（/）
5. 終了
________________
メニュー番号を選んでください:

3.操作を選択
・メニューに従って操作したい番号を選びます。（例：１）
・二つの数字を入力します。（例：55と22）。
・計算結果が出力されます。

4.終了する場合
・5を選択すると、終了確認が求められます。
・「はい」と答えるとプログラムが終了します。


実行例
1.足し算

$./computer.py
四則演算

___ 四則演算 ___
1. 足し算（＋）
2. 引き算（ー）
3. 掛け算（＊）
4. 割り算（/）
5. 終了
______________

メニュー番号を選んでください:1
１つ目の数字を入力してください:55
２つ目の数字を入力してください:22
計算結果: 77.0

2.割り算（エラー処理込み）
$ ./computer.py
四則演算

___ 四則演算 ___
1. 足し算（＋）
2. 引き算（ー）
3. 掛け算（＊）
4. 割り算（/）
5. 終了
________________
メニュー番号を選んでください:4
１つ目の数字を入力してください: 100
２つ目の数字を入力してください: 0
エラー: ０で割ることはできません


コードのポイント
1.メニュー表示関数

def show_menu():
    print("\n---　四則演算 ---")
    print("1.足し算（＋）")
    print("2.引き算（ー）")
    print("3.掛け算（＊）")
    print("4.割り算（/）")
    print("5.終了")
    print("--------------")

・この関数は、ユーザーに操作メニューを表示する。

2.計算ロジック

def perform_operation(choice, num1, num2):
    if choice == 1:
        return num1 + num2
    elif choice == 2:
        return num1 - num2
    elif choice == 3:
        return num1 * num2
    elif choice == 4:
        if num2 == 0:
            return "エラー: ０で割ることはできません"
        return num1 / num2
    else:
        return "その選択肢はありません。"


・入力された選択肢（choice）に基づいて計算を行います。
・割り算で０で割ることを防ぐため、エラーを表示します。

3.メイン処理

if __name__ == "__main__":
    main()

・プログラムのエントリー
・無限ループでユーザーからの入力を待ち、終了操作が行われたら終了します。
