# -*- coding:utf-8 -*-
"""
「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""

__author__ = "tina"
__version__ = "0.0.1"
__date__    = "2018/07/28" 


def test(target_str1="パトカー", target_str2="タクシー"):
    show_str = ""
    for str_i, str_j in zip(target_str1, target_str2):
        show_str += (str_i + str_j)
    print(show_str)
