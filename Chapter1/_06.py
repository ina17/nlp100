# -*- coding:utf-8 -*-
"""
集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""

__author__ = "tina"
__version__ = "0.0.1"
__date__    = "2018/07/28" 

from . import _05

def test(target_str01="paraparaparadise", target_str02="paragraph", in_check_str="se"):
    X = set(_05.get_n_gram(target=target_str01,n=2))
    Y = set(_05.get_n_gram(target=target_str02,n=2))
    
    print("XとYの和集合", X | Y)
    print("XとYの積集合", X & Y)
    print("XとYの差集合", X - Y)

    print("{0}というbigramは{1}と{2}のbi-gramの和集合に".format(in_check_str, target_str01, target_str02) , end="")
    print("含まれる") if in_check_str in (X | Y) else print("含まれない")
    