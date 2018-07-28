# -*- coding:utf-8 -*-
"""
n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""

__author__ = "tina"
__version__ = "0.0.1"
__date__    = "2018/07/28" 

def get_n_gram(target, n=2):
    result = [target[i:i+n] for i in range(0, len(target) - n + 1)]
    return result

def test(target_str="I am an NLPer"):
    words = target_str.strip().split()
    words_norm = [word.strip(",.") for word in words]

    print(get_n_gram(target=words_norm, n=2))
    print(get_n_gram(target=target_str, n=2))
