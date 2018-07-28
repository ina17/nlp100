# -*- coding:utf-8 -*-
"""
暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
    ・英小文字ならば(219 - 文字コード)の文字に置換
    ・その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""

__author__ = "tina"
__version__ = "0.0.1"
__date__    = "2018/07/28" 

def cipher(target_str):
    """
    暗号化/復号化ともに可能
    """
    result = ""
    for s in target_str:
        if s.islower():
            result += chr(219-ord(s))
        else:
            result += s
    return result


def test(target_str="CameRa"):
    print("対象文字列:\t", target_str)
    encode_str = cipher(target_str=target_str)
    print("暗号化:\t", encode_str)
    decode_str = cipher(target_str=encode_str)
    print("復号化:\t", decode_str)
