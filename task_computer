#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Takumi Sakata
# SPDX-License-Identifier: BSD-3-Clause

#!/usr/bin/python3
import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "エラー: ０で割ることはできません"
    return x / y

def main():
    # 標準入力からデータを読み取る
    input_data = sys.stdin.read().strip().split()
    if len(input_data) != 3:
        print("エラー: 入力は '操作 数値1 数値2' の形式で提供してください", file=sys.stderr)
        sys.exit(1)

    operation, num1, num2 = input_data
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("エラー: 数値1と数値2は有効な数値である必要があります", file=sys.stderr)
        sys.exit(1)

    if operation == "add":
        print(add(num1, num2))
    elif operation == "subtract":
        print(subtract(num1, num2))
    elif operation == "multiply":
        print(multiply(num1, num2))
    elif operation == "divide":
        print(divide(num1, num2))
    else:
        print("エラー: 有効な操作は 'add', 'subtract', 'multiply', 'divide' のいずれかです", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

