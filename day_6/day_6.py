#!/usr/bin/python
import sys
import copy

def read_input(input_file):
    with open(input_file, 'r') as file:
        return list(map(list, map(lambda x: x.rstrip(),  file.readlines())))

def print_map(m):
    print("%%%%%%%%%%")
    print("\n".join(list(map( lambda x: ''.join(x), m))))
    
def turn_right(d):
    if d[0] == -1:
        return (0, 1)
    elif d[1] == 1:
        return (1, 0)
    elif d[0] == 1:
        return (0, -1)
    elif d[1] == -1:
        return (-1, 0)

def has_loop(g_map, init, d):
    x, y = init
    counts = [[0 for i in range(len(g_map[0]))] for j in range(len(g_map))]
    run = True
    while run:
        if x + d[0] < 0 or x + d[0] >= len(g_map) or y + d[1] < 0 or y + d[1] >= len(g_map[x]):
            return False
        if counts[x + d[0]][y + d[1]] > 3:
            return True
        next = g_map[x + d[0]][y + d[1]]
        if next == '#':
            d = turn_right(d)
        else:
            counts[x][y] += 1
            x += d[0]
            y += d[1]
            
    
def task_1(input_file):
    g_map = read_input(input_file)
    # find starting position:
    x, y = (-1, -1)
    d = (-1, 0)
    count = 0
    for i, r in enumerate(g_map):
        for j, c in enumerate(r):
            if c == '^':
                g_map[i][j] = '.'
                x, y = i, j
                break
        if x != -1:
            break
    run = True
    init = (x, y)
    while run:
        # print_map(g_map)
        if x + d[0] < 0 or x + d[0] >= len(g_map) or y + d[1] < 0 or y + d[1] >= len(g_map[x]):
            g_map[x][y] = 'X'
            count += 1
            run = False
            break
        next = g_map[x + d[0]][y + d[1]]
        if next == '#':
            d = turn_right(d)
        elif next == '.' or next == 'X':
            if g_map[x][y] == '.':
                g_map[x][y] = 'X'
                count += 1
            x += d[0]
            y += d[1]
        else:
            print(f'UNEXPECTED VALUE {next} AT: {x + d[0]}, {y + d[1]}')
            break
    print(f'There are {count} unique positions')
    task_2(g_map, init, (-1, 0))

def task_2(g_map, init, d):
    count = 0
    x_count = 0
    for i, row in enumerate(g_map):
        for j, col in enumerate(row):
            if col == 'X':
                copy_map = copy.deepcopy(g_map)
                copy_map[i][j] = '#'
                if has_loop(copy_map, init, d):
                    count += 1
    print(f'there are {count} positons for an obstacle')

if __name__ == "__main__":
    input_file = 'input.txt'
    if sys.argv.count('-t'):
        input_file = 'test_input.txt'
    task_1(input_file)
