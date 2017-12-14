#!/usr/bin/python
import sys
sys.path.insert(0, '../')
from day10.part2 import knot_hash


def hex_to_bin(hex_str):
    return bin(int(hex_str, 16))[2:].zfill(4 * len(hex_str))


def count_bits_char(h):
    b = hex_to_bin(h)
    bit_sum = 0
    for c in b:
        bit_sum += int(c)
    return bit_sum


def count_bits(input_string):
    s = 0
    for c in input_string:
        s += count_bits_char(c)

    return s


def disk_defragmentation(input_string):
    cnt = 0
    rows = []
    for i in range(128):
        string = input_string + '-' + str(i)
        rows.append(knot_hash(string, 256))
        cnt += count_bits(rows[i])

    return cnt


if __name__ == '__main__':
    assert disk_defragmentation('flqrgnkx') == 8108

    with open(sys.argv[1]) as f:
        output = disk_defragmentation(f.read().strip())
        print('Output: {}'.format(output))
