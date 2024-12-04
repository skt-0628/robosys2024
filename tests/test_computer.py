#!/bin/bash -xv
# SPDX-FileCopyrightText: 2024 Takumi Sakata
# SPDX-License-Identifier: BSD-3-Clause

ng () {
    echo "${1}行目が違うよ"
    res=1
}

res=0

# テストケース1: 足し算
out=$(echo 3 2 | python3 ./computer.py add)
[ "${out}" = "5.0" ] || ng "$LINENO"

# テストケース2: 引き算
out=$(echo 5 2 | python3 ./computer.py subtract)
[ "${out}" = "3.0" ] || ng "$LINENO"

# テストケース3: 掛け算
out=$(echo 2 3 | python3 ./computer.py multiply)
[ "${out}" = "6.0" ] || ng "$LINENO"

# テストケース4: 割り算
out=$(echo 6 3 | python3 ./computer.py divide)
[ "${out}" = "2.0" ] || ng "$LINENO"

# テストケース5: ０で割る
out=$(echo 5 0 | python3 ./computer.py divide)
[ "$?" = 1 ] || ng "$LINENO"

# テストケース6: 数字以外の入力
out=$(echo 5 a | python3 ./computer.py add)
[ "$?" = 1 ] || ng "$LINENO"

# テストケース7: 空の入力
out=$(echo | python3 ./computer.py add)
[ "$?" = 1 ] || ng "$LINENO"

[ "${res}" = 0 ] && echo OK
exit $res

