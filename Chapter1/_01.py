# -*- coding:utf-8 -*-
"""
「パタトクカシーー」
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
"""

__author__ = "tina"
__version__ = "0.0.1"
__date__    = "2018/07/28" 

def test(target_str="パタトクカシーー"):
    show_str = ""
    for i in range(0, 8, 2):
        show_str += str(target_str)[i]
    print(show_str)
