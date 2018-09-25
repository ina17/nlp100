# -*- coding:utf-8 -*-
"""
形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）を
キーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

__author__ = "tina"
__version__ = "0.0.1"
__date__    = "2018/09/26" 

import MeCab
import re

def map_morpheme(target_file="Chapter4/neko.txt"):
    m = MeCab.Tagger()
    result = []
    with open(target_file, "r") as f:
        for i,line in enumerate(f):
            item = get_parse_line(m.parse(line))
            if len(item) > 0:
                result.append(item)
    return result

def get_parse_line(line):
    parse_lst = []
    items = re.split("[,\t\n]", line.strip())
    num = int(len(items) / 10)

    for i in range(num):
        parse_lst.append({"surface": items[10 * i],"base": items[10 * i + 7], "pos": items[10 * i + 1], "pos1": items[10 * i + 2]})
    return parse_lst
    
def test():
    print(map_morpheme())