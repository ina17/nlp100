# -*- coding:utf-8 -*-

import sys
from Chapter1 import _00, _01, _02, _03, _04, _05, _06, _07, _08, _09
from Chapter2 import _10, _11, _12, _13


if __name__ == "__main__":
    problem_idx = 13

    if len(sys.argv) == 2:
        problem_idx = int(sys.argv[1])
    print("言語処理100本ノック 問題{0:01d}の解答".format(problem_idx))
    method_name = "_{0:02d}.test".format(problem_idx)
    eval(method_name)()