# -*- coding:utf-8 -*-
"""
各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
確認にはcut, uniq, sortコマンドを用いよ．
"""

__author__ = "tina"
__version__ = "0.0.1"
__date__    = "2018/07/30" 

import numpy as np
from collections import Counter

def test(target_file="Chapter2/hightemp.txt"):

    with open(target_file, "r") as f:
        lines = f.readlines()

    items = [line.strip().split()[0] for line in lines]
    for item, count in Counter(items).most_common():
        idxes = [i for i, x in enumerate(items) if x == item]
        for idx in idxes:
            print(lines[idx], end="")



