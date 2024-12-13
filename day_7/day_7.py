#!/usr/bin/python
import sys
import re

def read_input(input_file):
    calibrations = []
    with open(input_file, 'r') as file:
        for line in file.readlines():
            result, nums = line.split(':')
            calibrations.append((int(result), list(map(int, re.findall(r'\d+', nums)))))
    return calibrations

def is_computable(res, curr, nums, concat=False):
    if len(nums) == 0:
        return res == curr
    if is_computable(res, curr + nums[0], nums[1:], concat) or is_computable(res, curr * nums[0], nums[1:], concat):
        return True
    if concat and is_computable(res, int(str(curr) + str(nums[0])), nums[1:], concat):
        return True
    return False
            
def task_1(input_file):
    calibrations = read_input(input_file)
    s = 0
    for res, nums in calibrations:
        if is_computable(res, nums[0], nums[1:]):
            s += res
    print(s)

def task_2(input_file):
    calibrations = read_input(input_file)
    s = 0
    for res, nums in calibrations:
        if is_computable(res, nums[0], nums[1:], concat=True):
            s += res
    print(s)

if __name__ == "__main__":
    input_file = 'input.txt'
    # input_file = 'test_input.txt'
    if sys.argv.count('-t'):
        input_file = 'test_input.txt'
    task_1(input_file)
    task_2(input_file)
