#!/usr/bin/python
import sys

def read_input(input_file):
    with open(input_file, 'r') as file:
        pass

def task_1(input_file):
    pass

def task_2(input_file):
    pass

if __name__ == "__main__":
    input_file = 'input.txt'
    if sys.argv.count('-t'):
        input_file = 'test_input.txt'
    task_1(input_file)
    task_2(input_file)
