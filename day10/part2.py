#!/usr/bin/python
import sys


def rotate(l, n):
    return l[n:] + l[:n]


def knot_hash(in_file):
    with open(in_file) as f:
        in_string = f.read().strip()

        lengths = [ord(c) for c in in_string]
        lengths = lengths + [17, 31, 73, 47, 23]

        my_list = list(range(256))
        curr_pos = 0
        skip = 0
        for t in range(64):
            for l in lengths:
                temp = list(reversed(rotate(my_list, curr_pos)[:l]))
                for i, v in enumerate(temp):
                    my_list[(curr_pos + i) % len(my_list)] = v
                curr_pos += l + skip
                while curr_pos > len(my_list):
                    curr_pos -= len(my_list)
                skip += 1

        # sparse -> dense
        dense = []
        for i in range(16):
            temp = 0
            for j in range(16):
                temp ^= my_list[16 * i + j]

            dense.append(temp)

        my_hash = []
        for d in dense:
            my_hash.append(hex(d)[2:])

    return ''.join(my_hash)


if __name__ == '__main__':
    output = knot_hash(sys.argv[1])
    print('Output: {}'.format(output))
