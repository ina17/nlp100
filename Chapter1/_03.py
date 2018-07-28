# -*- coding:utf-8 -*-
"""
円周率
"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
"""

__author__ = "tina"
__version__ = "0.0.1"
__date__    = "2018/07/28" 

def test(target_str="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."):
    words = target_str.strip().split()
    words_norm = [word.strip(",.") for word in words]
    print([len(word_norm) for word_norm in words_norm])
