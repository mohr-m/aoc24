#!/usr/bin/python
import sys
from itertools import pairwise

def read_input(input_file):
    """
    reads the input file and returns a list representing reports.
    Each report is a list consisting of multiple levels (int)
    """
    lines = []
    reports = []
    with open(input_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.rstrip()
        reports.append(list(map(int, line.split(' '))))

    return reports

def task_1(input_file):
    reports = read_input(input_file)
    safe_reports = 0                       
    for report in reports:
        gradients = list(map(lambda x: x[1]-x[0], pairwise(report)))
        if abs(sum(gradients)) == sum(map(abs, gradients)):
            # all gradients are either positiv or negative
            if len(list(filter(lambda x: 0 < abs(x) < 4, gradients))) == len(gradients):
                # all gradients are greater than 0 and smaller than 4
                safe_reports += 1
    print(f'There are {safe_reports} safe reports')

def task_2(input_file):
    pass

if __name__ == "__main__":
    input_file = 'input.txt'
    if sys.argv.count('-t'):
        input_file = 'test_input.txt'
    task_1(input_file)
    task_2(input_file)
