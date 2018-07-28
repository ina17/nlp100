# -*- coding:utf-8 -*-
"""
タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
"""

__author__ = "tina"
__version__ = "0.0.1"
__date__    = "2018/07/28" 

def test(target_file="Chapter2/hightemp.txt"):
    with open(target_file, "r") as f:
        print("結果")
        for line in f.readlines():
            print(line.replace("\t", " "), end="")
