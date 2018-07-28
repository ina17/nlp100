# -*- coding:utf-8 -*-
"""
行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
"""

__author__ = "tina"
__version__ = "0.0.1"
__date__    = "2018/07/28" 

import subprocess

def test(target_file="Chapter2/hightemp.txt"):
    with open(target_file, "r") as f:
        print("結果")
        print(len(f.readlines()))

    print("UNIXコマンドでの確認")
    subprocess.call(['wc', '-l', target_file])

