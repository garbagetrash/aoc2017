#!/usr/bin/python
from numba import jit
import sys


@jit
def gen(a, b):
    factorA = 16807
    factorB = 48271
    while True:
        a = (a * factorA) % 2147483647
        b = (b * factorB) % 2147483647

        yield a, b


@jit
def compare(a_init, b_init, N):
    cnt = 0
    idx = 0
    for a, b in gen(a_init, b_init):
        if a & 0xffff == b & 0xffff:
            cnt += 1

        idx += 1
        if idx >= N:
            return cnt


def parse(list_of_strings):
    a_init = int(list_of_strings[0].split()[-1])
    b_init = int(list_of_strings[1].split()[-1])
    return a_init, b_init


def dueling_generators(list_of_strings):
    a_init, b_init = parse(list_of_strings)
    return compare(a_init, b_init, 40000000)


if __name__ == '__main__':
    assert dueling_generators(['Generator A starts with 65',
                               'Generator B starts with 8921']) == 588

    with open(sys.argv[1]) as f:
        output = dueling_generators([l.strip() for l in f.readlines()])
        print('Output: {}'.format(output))
