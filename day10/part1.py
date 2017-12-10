#!/usr/bin/python
import sys


def rotate(l, n):
    return l[n:] + l[:n]


def knot_hash(in_file):
    with open(in_file) as f:
        in_string = f.read().strip()

        lengths = list(map(lambda x: int(x), in_string.split(',')))
        my_list = list(range(256))
        curr_pos = 0
        skip = 0

        for l in lengths:
            temp = list(reversed(rotate(my_list, curr_pos)[:l]))
            for i, v in enumerate(temp):
                my_list[(curr_pos + i) % len(my_list)] = v
            curr_pos += l + skip
            while curr_pos > len(my_list):
                curr_pos -= len(my_list)
            skip += 1

    return my_list[0] * my_list[1]


if __name__ == '__main__':
    output = knot_hash(sys.argv[1])
    print('Output: {}'.format(output))
