import subprocess

def test_addition():
    result = subprocess.run(
        ["python3", "computer.py"],
        input="1\n10\n20\n5\nはい\n",
        text=True,
        capture_output=True
    )
    assert "計算結果:30.0" in result.stdout

def test_division_by_zero():
    result = subprocess.run(
        ["python3", "computer.py"],
        input="4\n10\n0\n5\nはい\n",
        text=True,
        capture_output=True
    )
    assert "エラー: ０で割ることはできません" in result.stdout

def test_invalid_input():
    result = subprocess.run(
        ["python3", "computer.py"],
        input="9\n5\nはい\n",
        text=True,
        capture_output=True
    )
    assert "エラー:無効な番号です。" in result.stdout

