#!/usr/bin/python
import sys
import numpy as np

def read_input(input_file):
    with open(input_file, 'r') as file:
        return list(map(lambda x: list(x.rstrip()), file.readlines()))

def print_map(m):
    print("%%%%%%%%%%")
    print("\n".join(list(map( lambda x: ''.join(x), m))))

def task_1(input_file):
    f_map = read_input(input_file)
    freqs = {}
    antinodes = set()
    cols = len(f_map[0])
    rows = len(f_map)
    for i, row in enumerate(f_map):
        for j, cell in enumerate(row):
            if cell != '.':
                freqs.setdefault(cell, [])
                freqs[cell].append(np.array([i, j]))
    for freq, locs in freqs.items():
        for a in range(len(locs)):
            for b in range(a + 1, len(locs)):
                d = locs[a] - locs[b]
                a1 = locs[a] + d
                a2 = locs[b] - d
                if 0 <= a1[0] < rows and 0 <= a1[1] < cols:
                    antinodes.add(str(locs[a] + d))
                    f_map[a1[0]][a1[1]] = '#'
                if 0 <= a2[0] < rows and 0 <= a2[1] < cols:
                    f_map[a2[0]][a2[1]] = '#'
                    antinodes.add(str(locs[b] - d))
    print(len(antinodes))
    # print_map(f_map)
    

def task_2(input_file):
    f_map = read_input(input_file)
    freqs = {}
    antinodes = set()
    cols = len(f_map[0])
    rows = len(f_map)
    if rows != cols:
        print(f'cols ({cols}) =!= rows ({rows})')
    for i, row in enumerate(f_map):
        for j, cell in enumerate(row):
            if cell != '.':
                freqs.setdefault(cell, [])
                freqs[cell].append(np.array([i, j]))
    for freq, locs in freqs.items():
        for a in range(len(locs)):
            for b in range(a + 1, len(locs)):
                d = locs[a] - locs[b]
                i = 0
                while 0 <= min(locs[a] + d * i) and max(locs[a] + d * i) < rows:
                    antinodes.add(str(locs[a] + d * i))
                    i += 1
                i = 0
                while 0 <= min(locs[a] - d * i) and max(locs[a] - d * i) < rows:
                    antinodes.add(str(locs[a] - d * i))
                    i += 1
    print(len(antinodes))
        

if __name__ == "__main__":
    input_file = 'input.txt'
    if sys.argv.count('-t'):
        input_file = 'test_input.txt'
    task_1(input_file)
    task_2(input_file)
