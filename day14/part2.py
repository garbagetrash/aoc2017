#!/usr/bin/python
import sys
sys.path.insert(0, '../')
from day10.part2 import knot_hash
from day12.part2 import Graph, Node
import numpy as np


def hex_to_bin(hex_str):
    return bin(int(hex_str, 16))[2:].zfill(4 * len(hex_str))


def count_groups(arr):
    graph = Graph()
    for i in range(128):
        for j in range(128):
            if arr[i, j] > 0:
                id_num = 128 * i + j
                graph.add_node(id_num)
                narr = check_neighbors(i, j, arr)
                for n in narr:
                    graph.connect(id_num, 128 * n[0] + n[1])

    return graph.count_groups()


def check_neighbors(i, j, arr):
    narr = []
    if j < 127 and arr[i, j + 1] > 0:
        narr.append((i, j + 1))

    if j > 0 and arr[i, j - 1] > 0:
        narr.append((i, j - 1))

    if i < 127 and arr[i + 1, j] > 0:
        narr.append((i + 1, j))

    if i > 0 and arr[i - 1, j] > 0:
        narr.append((i - 1, j))

    return narr


def disk_defragmentation(input_string):
    rows = np.zeros((128, 128))
    for i in range(128):
        string = input_string + '-' + str(i)
        rows[i, :] = [int(c) for c in hex_to_bin(knot_hash(string, 256))]

    return count_groups(rows)


if __name__ == '__main__':
    assert disk_defragmentation('flqrgnkx') == 1242

    with open(sys.argv[1]) as f:
        output = disk_defragmentation(f.read().strip())
        print('Output: {}'.format(output))
