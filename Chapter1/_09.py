# -*- coding:utf-8 -*-
"""
Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
"""

__author__ = "tina"
__version__ = "0.0.1"
__date__    = "2018/07/28" 

import numpy as np

def typoglycemia(target_str):
    result_str = ""
    words = target_str.strip().split()
    length = np.array([len(word) for word in words])

    length[[0,len(length)-1]] = 0
    idx = np.where(length > 4)[0]

    els = set(range(len(words)))-set(idx)

    np.random.shuffle(idx)
    for i in els:
        idx = np.insert(idx, i,i)

    for i in idx:
        result_str += words[i] + " "
    return result_str  

def test(target_str="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."):
    print("変更前:", target_str)
    print("変更後:", typoglycemia(target_str=target_str))
