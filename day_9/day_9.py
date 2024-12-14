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

def move_blocks(f_map):
    for i, m in enumerate(f_map):
        f_map[i] = (int(i/2) if i % 2 == 0 else None, int(m))
    i = len(f_map) - 1
    while i > 0:
        if f_map[i][0] == None:
            i -= 1
            continue
        for j in range(0, i):
            v = f_map[j]
            if v[0] == None and v[1] >= f_map[i][1]:
                rest = v[1] - f_map[i][1]
                f_map[j] = f_map[i]
                if rest: 
                    f_map.insert(j+1, (None, rest))
                    f_map[i + 1] = (None, f_map[j][1])
                    i += 1
                else:
                    f_map[i] = (None, f_map[j][1])
                break
        i -= 1
    return f_map

def f_map2str(f):
    res = []
    for m in f:
        res.extend([m[0]] * m[1])
    return res

def mem_checksum(memory):
    res = 0
    for i, mi in enumerate(memory):
        if mi != None:
            res += i * mi
    return res

def f_map_checksum(mem_str):
    res = 0
    for i, v in enumerate(mem_str):
        if v != None:
            res += i * v
    return res
    
def task_1(input_file):
    f_map = read_input(input_file)
    memory = build_memory(f_map)
    print(mem_checksum(defrag_memory(memory)))

def task_2(input_file):
    f_map = list(read_input(input_file))
    print(f_map_checksum(f_map2str(move_blocks(f_map))))

if __name__ == "__main__":
    input_file = 'input.txt'
    if sys.argv.count('-t'):
        input_file = 'test_input.txt'
    task_1(input_file)
    task_2(input_file)
