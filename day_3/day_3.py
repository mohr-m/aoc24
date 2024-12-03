#!/usr/bin/python
import sys
import re

def read_input(input_file):
    with open(input_file, 'r') as file:
        return file.read()

def task_1(input_file):
    input = read_input(input_file)
    mul_re = re.compile(r'mul\((\d+),(\d+)\)')
    result = 0
    for m in mul_re.finditer(input):
        result += int(m.group(1)) * int(m.group(2))
    print(f'task_1 - result: {result}')
    

def task_2(input_file):
    input = read_input(input_file)
    mul_re = re.compile(r"mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)")
    result = 0
    do = True
    for m in mul_re.finditer(input):
        if m.group(0) == 'do()':
            do = True
        elif m.group(0) == 'don\'t()':
            do = False
        elif do:
            result += int(m.group(1)) * int(m.group(2))
    print(f'task_2 - result: {result}')

if __name__ == "__main__":
    input_file = 'input.txt'
    if sys.argv.count('-t'):
        input_file = 'test_input.txt'
    task_1(input_file)
    task_2(input_file)
