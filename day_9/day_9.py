#!/usr/bin/python
import sys

def read_input(input_file):
    with open(input_file, 'r') as file:
        return file.readline().rstrip()

def build_memory(f_map):
    memory = []
    m_index = 0
    for i, c in enumerate(f_map):
        if i % 2 != 0:
            memory.extend([None] * int(c))
        else:
            memory.extend([m_index] * int(c))
            m_index += 1
    return memory

def defrag_memory(memory):
    j = 0
    # breakpoint()
    for i in range(len(memory)-1, -1, -1):
        if i < j:
            break
        if memory[i] != None:
            while j+1 < i and memory[j] != None:
                j += 1
            if memory[j] != None:
                break
            memory[j] = memory[i]
            memory[i] = None
    return memory

def checksum_of(memory):
    res = 0
    for i, mi in enumerate(memory):
        if mi != None:
            res += i * mi
    return res
    
def task_1(input_file):
    f_map = read_input(input_file)
    memory = build_memory(f_map)
    print(checksum_of(defrag_memory(memory)))
    

def task_2(input_file):
    pass

if __name__ == "__main__":
    input_file = 'input.txt'
    if sys.argv.count('-t'):
        input_file = 'test_input.txt'
    task_1(input_file)
    task_2(input_file)
