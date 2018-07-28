# -*- coding:utf-8 -*-
"""
col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．
"""

__author__ = "tina"
__version__ = "0.0.1"
__date__    = "2018/07/28" 

import subprocess

def test(target_file1="Chapter2/col1.txt",
        target_file2="Chapter2/col2.txt",
        output_file="Chapter2/col1and2.txt"):

    with open(target_file1, "r") as f1:
        lines1 = f1.readlines()
    with open(target_file2, "r") as f2:
        lines2 = f2.readlines()

    with open(output_file, "w") as f:
        for line1, line2 in zip(lines1, lines2):
            f.write(line1.strip()+"\t"+line2.strip()+"\n")

    print("UNIXコマンドでの確認")
    subprocess.call(['paste', '-d', '\t', target_file1, target_file2])
