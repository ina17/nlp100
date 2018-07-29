# -*- coding:utf-8 -*-
"""
先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
確認にはheadコマンドを用いよ．
"""

__author__ = "tina"
__version__ = "0.0.1"
__date__    = "2018/07/29" 

import subprocess

def show_head(lines, n_lines=10):
    for line in lines[:n_lines]:
        print(line.strip())

def test(target_file="Chapter2/hightemp.txt", n_lines=10):

    with open(target_file, "r") as f:
        lines = f.readlines()
    show_head(lines, n_lines=n_lines)

    print("UNIXコマンドでの確認")
    subprocess.call(['head', '-n', str(n_lines), target_file])

