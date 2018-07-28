# -*- coding:utf-8 -*-
"""
1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
"""

__author__ = "tina"
__version__ = "0.0.1"
__date__    = "2018/07/28" 

import subprocess

def save_col(lines, output_file, col_idx):
    with open(output_file, "w") as fw:
        for line in lines:
            row = line.strip().split("\t")
            fw.write(row[col_idx-1]+"\n")


def test(target_file="Chapter2/hightemp.txt",
        output_file1="Chapter2/col1.txt",
        output_file2="Chapter2/col2.txt"):

    with open(target_file, "r") as f:
        lines = f.readlines()

        save_col(lines=lines, output_file=output_file1, col_idx=1)
        save_col(lines=lines, output_file=output_file2, col_idx=2)

    print("UNIXコマンドでの確認")
    print(output_file1)
    subprocess.call(['cut', '-f', '1', target_file])
    print(output_file2)
    subprocess.call(['cut', '-f', '2', target_file])
