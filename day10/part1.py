#!/usr/bin/python
import sys


def rotate(l, n):
    return l[n:] + l[:n]


def hash_round(curr_pos, skip, lengths, my_list):
    for l in lengths:
        temp = list(reversed(rotate(my_list, curr_pos)[:l]))
        for i, v in enumerate(temp):
            my_list[(curr_pos + i) % len(my_list)] = v
        curr_pos += l + skip
        while curr_pos > len(my_list):
            curr_pos -= len(my_list)
        skip += 1


def knot_hash(input_string, circular_list_len):
    lengths = list(map(lambda x: int(x), input_string.split(',')))
    my_list = list(range(circular_list_len))
    curr_pos = 0
    skip = 0

    hash_round(curr_pos, skip, lengths, my_list)

    return my_list[0] * my_list[1]


if __name__ == '__main__':
    assert knot_hash('3,4,1,5', 5) == 12

    with open(sys.argv[1]) as f:
        output = knot_hash(f.read().strip(), 256)
        print('Output: {}'.format(output))
