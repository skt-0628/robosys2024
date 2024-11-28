#!/usr/bin/python3
def show_menu():
    print("\n---　四則演算 ---")
    print("1.足し算（＋）")
    print("2.引き算（ー）")
    print("3.掛け算（＊）")
    print("4.割り算（/）")
    print("5.終了")
    print("--------------")


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


def main():
    print("四則演算")

    while True:
        show_menu()
        try:
            choice = int(input("メニュー番号を選んでください:").strip())
            if choice == 5:
                confirm = input("本当に終了しますか？（はい/いいえ）:").strip()
                if confirm.lower() in ["はい", "ｙ","yes"]:
                    print("プログラムを終了します。")
                    break
                else:
                    print("終了をキャンセルしました。続けます。")
                    continue
            if choice not in [1,2,3,4]:
                print("エラー:無効な番号です。１～５の番号を選んでください。")
                continue

            num1 = float(input("１つ目の数字を入力してください:").strip())
            num2 = float(input("２つ目の数字を入力してください:").strip())
            result = perform_operation(choice, num1, num2)


            if isinstance(result,str):
                print(result)
            else:
                print(f"計算結果:{result}")

        except ValueError:
            print("エラー:無効です。正しい操作を行ってください。")
        except Exception as e:
            print(f"予期しないエラーが発生しました: {e}")



if __name__ == "__main__":
    main() 
   

