# -*- coding:utf-8 -*-
"""
ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
同様の処理をsplitコマンドで実現せよ．
"""

__author__ = "tina"
__version__ = "0.0.1"
__date__    = "2018/07/29" 

import subprocess

def show_splits(lines, n_splits=10):
    for i in range(0, len(lines), n_splits):
        print("分割表示")
        start_idx = i
        end_idx = i+n_splits if i+n_splits > len(lines) else len(lines)

        for line in lines[start_idx:end_idx]:
            print(line.strip())

def test(target_file="Chapter2/hightemp.txt", n_splits=10):

    with open(target_file, "r") as f:
        lines = f.readlines()
    show_splits(lines, n_splits=n_splits)

    print("UNIXコマンドでの確認")
    subprocess.call(['split', '-l', str(n_splits), target_file, 'Chapter2/split'])
