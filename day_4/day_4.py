#!/usr/bin/python
import sys

def read_input(input_file):
    lines = []
    with open(input_file, 'r') as file:
        return list(map(list, file.read().split('\n')))

def check_xmas(mat, i, j, c):
    count = 0
    # vorwärts
    if j + 4 <= len(mat[i]) and ''.join(mat[i][j:j+4]) == 'XMAS':
        count += 1
    # rückwärts
    if j >= 3 and ''.join(mat[i][j:j-4:-1]) == 'XMAS':
        count += 1
    # runter
    if i + 4 <= len(mat) and mat[i][j] + mat[i+1][j] + mat[i+2][j] + mat[i+3][j] == 'XMAS':
        count += 1
    # hoch
    if i >= 3 and mat[i][j] + mat[i-1][j] + mat[i-2][j] + mat[i-3][j] == 'XMAS':
        count += 1
    # runter rechts
    if i + 4 <= len(mat) and j + 4 <= len(mat[i]) and mat[i][j] + mat[i+1][j+1] + mat[i+2][j+2] + mat[i+3][j+3] == 'XMAS':
        count += 1
    # runter links
    if i + 4 <= len(mat) and j >= 3 and mat[i][j] + mat[i+1][j-1] + mat[i+2][j-2] + mat[i+3][j-3] == 'XMAS':
        count += 1
    # hoch rechts
    if i >= 3 and j + 4 <= len(mat[i]) and mat[i][j] + mat[i-1][j+1] + mat[i-2][j+2] + mat[i-3][j+3] == 'XMAS':
        count += 1
    # hoch links
    if i >= 3 and j >= 3 and mat[i][j] + mat[i-1][j-1] + mat[i-2][j-2] + mat[i-3][j-3] == 'XMAS':
        count += 1
    return count

def task_1(input_file):
    mat = read_input(input_file)
    count = 0
    for i, l in enumerate(mat):
        for j, c in enumerate(l):
            if c == 'X':
                count += check_xmas(mat, i, j, c)
    print(count)


import numpy as np
def task_gpt(input_file):

    # Die Matrix als 2D-Array darstellen
    matrix_string = """
    XMASXMAS
    MASXMASX
    ASXMASXM
    SXMASXMA
    XMASXMAS
    MASXMASX
    ASXMASXM
    SXMASXMA
    """
    with open('input.txt') as f:
        matrix_string = f.read()

    # Zielwort
    target = "XMAS"

    # Matrix erstellen
    lines = [line.strip() for line in matrix_string.strip().split('\n')]
    matrix = np.array([list(line) for line in lines])

    # Matrixgröße
    rows, cols = matrix.shape

    # Alle Suchrichtungen
    directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]

    # Wort in allen Richtungen zählen
    total_count = sum(count_word_in_direction(matrix, target, dx, dy) for dx, dy in directions)
    print(total_count)

# Funktion zur Suche nach dem Wort in einer bestimmten Richtung
def count_word_in_direction(matrix, word, dx, dy):
    count = 0
    word_len = len(word)
    rows, cols = matrix.shape
    
    for x in range(rows):
        for y in range(cols):
            found = True
            for k in range(word_len):
                nx, ny = x + k * dx, y + k * dy
                if not (0 <= nx < rows and 0 <= ny < cols) or matrix[nx, ny] != word[k]:
                    found = False
                    break
            if found:
                count += 1
    return count


def task_2(input_file):
    pass

if __name__ == "__main__":
    input_file = 'input.txt'
    if sys.argv.count('-t'):
        input_file = 'test_input.txt'
    # task_1(input_file)
    # task_2(input_file)
    task_gpt(0)
