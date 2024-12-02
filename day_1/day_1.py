#!/usr/bin/python
import re
import sys

def read_input(filename):
    """
    Args:
    filename: the name of the input file

    Returns:
    a tuple consisting of two lists: the numbers on the left and the right side of the input
    """
    lines = []
    left = []
    right = []
    line_split_re = re.compile(r'^(\d+)   (\d+)$')
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in lines:
        line_match = line_split_re.match(line)
        left.append(int(line_match.group(1)))
        right.append(int(line_match.group(2)))
    return (left, right)

def task_1(input_file):
    """
    Calculate the total distance of all pairs in the input file
    A pair is defined as the first, second, third, ... pair of smallest numbers on the left and right side
    """
    left, right = read_input(input_file)
    distance = 0
    while len(left):
        min_left, min_right = (min(left), min(right))
        left.remove(min_left)
        right.remove(min_right)
        distance += abs(min_left - min_right)
    print(f'Total distance: {distance}')

def task_2(input_file):
    """
    """
    left, right = read_input(input_file)
    similarity_score = 0
    for num in left:
        similarity_score += num * right.count(num)
    print(f'Similarity score: {similarity_score}')        

if __name__ == '__main__':
    input_file = 'input.txt'
    if sys.argv.count('-t'):
        input_file = 'test_input.txt'
    task_1(input_file)
    task_2(input_file)
