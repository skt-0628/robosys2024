#!/bin/bash -xv
# SPDX-FileCopyrightText: 2024 Takumi Sakata
# SPDX-License-Identifier: BSD-3-Clause

ng () {
    echo "${1}行目が違うよ"
    res=1
}

res=0

# テストケース1: 足し算
out=$(echo "add 3 4" | python3 ./computer.py)
[ "${out}" = "7.0" ] || ng "$LINENO"

# テストケース2: 引き算
out=$(echo "subtract 10 3" | python3 ./computer.py)
[ "${out}" = "7.0" ] || ng "$LINENO"

# テストケース3: 掛け算
out=$(echo "multiply 2 5" | python3 ./computer.py)
[ "${out}" = "10.0" ] || ng "$LINENO"

# テストケース4: 割り算
out=$(echo "divide 9 3" | python3 ./computer.py)
[ "${out}" = "3.0" ] || ng "$LINENO"

# テストケース5: 0で割る
out=$(echo "divide 5 0" | python3 ./computer.py)
[ "${out}" = "エラー: ０で割ることはできません" ] || ng "$LINENO"

# テストケース6: 無効な操作
out=$(echo "mod 5 2" | python3 ./computer.py 2>&1)
[ "${out}" = "エラー: 有効な操作は 'add', 'subtract', 'multiply', 'divide' のいずれかです" ] || ng "$LINENO"

# テストケース7: 無効な入力
out=$(echo "add a b" | python3 ./computer.py 2>&1)
[ "${out}" = "エラー: 数値1と数値2は有効な数値である必要があります" ] || ng "$LINENO"


[ "${res}" = 0 ] && echo "OK"
exit $res

