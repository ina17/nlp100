# -*- coding:utf-8 -*-
"""
各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
"""

__author__ = "tina"
__version__ = "0.0.1"
__date__    = "2018/07/29" 

import numpy as np

def test(target_file="Chapter2/hightemp.txt", n_splits=10):

    with open(target_file, "r") as f:
        lines = f.readlines()

    items = [float(line.strip().split()[2]) for line in lines]
    for i in np.argsort(items)[::-1]:
        print(lines[i], end="")


