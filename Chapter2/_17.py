# -*- coding:utf-8 -*-
"""
１列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
"""

__author__ = "tina"
__version__ = "0.0.1"
__date__    = "2018/07/29" 


def test(target_file="Chapter2/hightemp.txt", n_splits=10):

    with open(target_file, "r") as f:
        lines = f.readlines()

    items = set([line.strip().split()[0] for line in lines])
    for item in items:
        print(item)

