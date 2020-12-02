#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day02.py: Advent of Code 2020 --- Day 2: Password Philosophy ---
   https://adventofcode.com/2020/day/2
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import advent
from utils import *

def download_input_data():
    global fin
    global lines
    advent.setup(2020, 2, dry_run=False)
    fin = advent.get_input()
    lines = get_lines(fin.readlines())
    

def parse_pasw_line(psw_line):
    rule, psw = psw_line.split(":")
    accuracy, character = rule.split(" ")
    min, max = accuracy.split("-")
    #print(f"{min} {max} {psw.count(character)}")
    return int(min), int(max), character, psw.strip()

def part01():
    global fin 
    global lines
    global total
    total = 0
    for psw_line in lines:
        min, max, character, psw = parse_pasw_line(psw_line)
        if psw.count(character) in range(min, max+1):
            total +=1
    assert total == 628
    advent.submit_answer(1, total)

def part02():
    global fin 
    global nums
    global total
    total = 0
    for psw_line in lines:
        min, max, character, psw = parse_pasw_line(psw_line)
        if ((psw[min-1] == character) or (psw[max-1] == character)) and not((psw[min-1] == character) and (psw[max-1] == character)):
            total += 1
    assert total == 705
    advent.submit_answer(2, total)

if __name__ == "__main__":
    download_input_data()
    timer_start()
    part01()
    part02()
