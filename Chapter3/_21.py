# -*- coding:utf-8 -*-
"""
JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""

__author__ = "tina"
__version__ = "0.0.1"
__date__    = "2018/08/01" 

import json

def test(target_file="Chapter3/jawiki-country.json"):
    with open(target_file, "r") as f:
        wiki = {i: json.loads(line) for i,line in enumerate(f)}
    
    for key, value in wiki.items():
        if value["title"] == "イギリス":
            

if __name__ == "__main__":
    test()