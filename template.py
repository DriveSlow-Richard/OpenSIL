#! -*- coding:utf-8 -*-

# ======================
# -- Comment -----------
# ======================

"""
# Copyrights: che_lu_man_man
# Description: to do something.
# Author: limanman is a good man.
# Date: 2022-12-12
"""

# ======================
# -- import ------------
# ======================
import glob
import os
import sys
import time
import argparse


# ======================
# -- Functions----------
# ======================

def function_001():
    pass


def function_002():
    pass


# ======================
# -- game_loop() -------
# ======================
def game_loop(args):
    try:
        pass

    finally:
        pass


# ======================
# -- main() ------------
# ======================
def main():
    # 打印该脚本的用法
    print(__doc__)
    # 设置命令行输入参数
    my_argparser = argparse.ArgumentParser()
    my_argparser.add_argument('-f', '--file', default=None, help='input the file name to get config parameters.')
    my_argparser.add_argument('-n', '--name', default="limanman", help='input name to give permission.')
    my_args = my_argparser.parse_args()
    # 进入主循环
    try:
        game_loop(my_args)
    except KeyboardInterrupt:
        print('\nCancelled by user. Bye!')


# ======================
# -- Execution ---------
# ======================
if __name__ == '__main__':
    main()
