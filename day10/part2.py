#!/usr/bin/python
from numba import jit
import numpy as np
import sys


def rotate(l, n):
    return l[n:] + l[:n]


@jit
def flip(my_list, curr_pos, l):
    if l % 2 == 0:
        r = l / 2
    else:
        r = (l - 1) / 2

    for i in range(int(r)):
        start_idx = (curr_pos + i) % len(my_list)
        stop_idx = (curr_pos + l - i - 1) % len(my_list)
        temp = my_list[start_idx]
        my_list[start_idx] = my_list[stop_idx]
        my_list[stop_idx] = temp

    return my_list


@jit
def hash_round(curr_pos, skip, lengths, my_list):
    for l in lengths:
        my_list = flip(my_list, curr_pos, l)
        curr_pos += l + skip
        while curr_pos > len(my_list):
            curr_pos -= len(my_list)
        skip += 1

    return curr_pos, skip, my_list


def knot_hash(input_string, circular_list_len=256):
    lengths = [ord(c) for c in input_string]
    lengths = lengths + [17, 31, 73, 47, 23]

    my_list = np.array(list(range(circular_list_len)))
    curr_pos = 0
    skip = 0
    for t in range(64):
        curr_pos, skip, my_list = hash_round(curr_pos, skip, lengths, my_list)

    # sparse -> dense
    dense = []
    for i in range(16):
        temp = 0
        for j in range(16):
            temp ^= my_list[16 * i + j]

        dense.append(temp)

    my_hash = []
    for d in dense:
        my_hash.append('{:02x}'.format(d))

    output = ''.join(my_hash)
    return output


if __name__ == '__main__':
    assert knot_hash('', 256) == 'a2582a3a0e66e6e86e3812dcb672a272'
    assert knot_hash('AoC 2017', 256) == '33efeb34ea91902bb2f59c9920caa6cd'
    assert knot_hash('1,2,3', 256) == '3efbe78a8d82f29979031a4aa0b16a9d'
    assert knot_hash('1,2,4', 256) == '63960835bcdc130f0b66d7ff4f6a5a8e'

    with open(sys.argv[1]) as f:
        output = knot_hash(f.read().strip(), 256)
        print('Output: {}'.format(output))
