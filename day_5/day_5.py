#!/usr/bin/python
import sys
import re

def read_input(input_file):
    rule_re = re.compile(r'(\d+)\|(\d+)')
    number_re = re.compile(r'(\d+)')
    rules = dict()
    updates = dict()
    with open(input_file, 'r') as file:
        for line in file.readlines():
            if m := rule_re.match(line):
                if rules.setdefault(m.group(1), False):
                    rules[m.group(1)] += '|' + m.group(2)
                else:
                    rules[m.group(1)] = m.group(2)
            elif m := number_re.match(line):
                updates[line] = list(map(int, number_re.findall(line)))
    return (rules, updates)

def is_incorrect(line, rules):
    """
    searches the line for a rule in rules which matches this line and returns the corresponding key.
    If no rule matches, hence the line is correct, it returns None
    """
    for number, rule in rules.items():
        rule_re = re.compile(f'.*({rule}).*{number}.*')
        if rule_re.match(line):
            return number
    return None

def move_to_front(lst, idx):
    if idx > 0 and idx < len(lst):
        lst[idx - 1] ^= lst[idx]
        lst[idx] ^= lst[idx - 1]
        lst[idx - 1] ^= lst[idx]
    return lst, ','.join(list(map(str, lst)))

def task_1(input_file):
    rules, updates = read_input(input_file)
    sum = 0
    for update, nums in updates.items():
        if not is_incorrect(update, rules):
            sum += nums[int(len(nums)/2)]
    print(f'task_1: {sum}')
    
def task_2(input_file):
    rules, updates = read_input(input_file)
    sum = 0
    for update, nums in updates.items():
        if is_incorrect(update, rules):
            while num := is_incorrect(update, rules):
                nums, update = move_to_front(nums, nums.index(int(num)))
            sum += nums[int(len(nums)/2)]
    print(f'task_2: {sum}')

if __name__ == "__main__":
    input_file = 'input.txt'
    if sys.argv.count('-t'):
        input_file = 'test_input.txt'
    task_1(input_file)
    task_2(input_file)
