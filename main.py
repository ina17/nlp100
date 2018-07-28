# -*- coding:utf-8 -*-

from Chapter1 import _00, _01, _02, _03, _04, _05, _06, _07, _08, _09


if __name__ == "__main__":
    problem_idx = 6

    method_name = "_{0:02d}.test".format(problem_idx)
    eval(method_name)()