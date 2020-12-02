#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day01.py: Advent of Code 2020 --- Day 1: Report Repair ---
   https://adventofcode.com/2020/day/1
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import advent
from utils import *

def download_input_data():
    global fin
    global nums    
    advent.setup(2020, 1, dry_run=False)
    fin = advent.get_input()
    nums = list(map(int, fin.readlines()))
    

def part01():
    global fin 
    global nums
    global total
    for idx0, num0 in enumerate(nums):
        for idx1, num1 in enumerate(nums):
                if (idx0 != idx1) and ((num0 + num1) == 2020):
                    total = num0 * num1
                    break
        else:
            continue
        break
    assert total == 1020084
    advent.submit_answer(1, total)

def part02():
    global fin 
    global nums
    global total
    for idx0, num0 in enumerate(nums):
        for idx1, num1 in enumerate(nums):
            for idx2, num2 in enumerate(nums):
                if (idx0 != idx1) and ((num0 + num1 + num2) == 2020):
                    total = num0 * num1 * num2
                    break
            else:
                continue
            break
        else:
            continue
        break
    assert total == 295086480
    advent.submit_answer(2, total)

if __name__ == "__main__":
    download_input_data()
    timer_start()
    part01()
    part02()
