# -*- coding:utf-8 -*-
"""
動詞の原形
動詞の原形をすべて抽出せよ．
"""

__author__ = "tina"
__version__ = "0.0.1"
__date__    = "2018/09/26" 

from . import _30

def test(target_file="Chapter4/neko.txt"):
    parse_lst = _30.map_morpheme(target_file=target_file)
    parse_lst = [flatten for inner in parse_lst for flatten in inner]
    result = [item["surface"] for item in parse_lst if item["pos"] == "名詞" and item["pos1"] == "サ変接続"]
    print(result)
