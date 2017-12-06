#!/usr/bin/python
import sys
import numpy as np


def realloc(l):
    idx = np.argmax(l)
    val = np.max(l)
    l[idx] = 0

    for i in range(val):
        l[(idx + i + 1) % len(l)] += 1

    return l


def memory_banks(in_file):
    with open(in_file) as f:
        in_string = f.read().strip()
        banks = list(map(lambda x: int(x), in_string.split()))

        cnt = 1
        state_dict = {}
        while True:
            banks = realloc(banks)
            tbanks = tuple(banks)
            if tbanks in state_dict:
                return cnt
            state_dict[tbanks] = 1
            cnt += 1


if __name__ == '__main__':
    output = memory_banks(sys.argv[1])
    print('Output: {}'.format(output))
