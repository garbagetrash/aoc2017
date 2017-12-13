#!/usr/bin/python
from numba import jit
import sys


def parse_line(line, sdict, max_depth):
    vals = [int(x.rstrip(':')) for x in line.split()]
    sdict[vals[0]] = vals[1]

    if vals[0] > max_depth:
        return vals[0]
    else:
        return max_depth


def parse_input(list_of_strings):
    sdict = {}
    max_depth = 0
    for line in list_of_strings:
        max_depth = parse_line(line, sdict, max_depth)

    return sdict, max_depth


def name(list_of_strings):

    sdict, max_depth = parse_input(list_of_strings)

    speriods = []
    for t in range(max_depth + 1):
        if t in sdict:
            period = (sdict[t] - 1) * 2
            speriods.append(period)
        else:
            speriods.append(-1)

    return find_delay(speriods, max_depth)


@jit
def find_delay(speriods, max_depth):
    delay = 0
    while True:
        found = False
        for p in range(max_depth + 1):
            if speriods[p] > 0:
                if (delay + p) % speriods[p] == 0:
                    found = True
                    break
        if not found:
            return delay
        else:
            delay += 1


if __name__ == '__main__':
    assert name(['0: 3', '1: 2', '4: 4', '6: 4']) == 10

    with open(sys.argv[1]) as f:
        output = name([l.strip() for l in f.readlines()])
        print('Output: {}'.format(output))