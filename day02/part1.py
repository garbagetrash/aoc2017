#!/usr/bin/python
import sys


def sum_diffs(in_file):
    sumof = []
    with open(in_file) as f:
        str_list = list(map(lambda x: x.strip(), f.readlines()))
        for s in str_list:
            line = list(map(lambda x: float(x), s.split()))
            minlist = min(line)
            maxlist = max(line)
            diff = maxlist - minlist
            sumof.append(diff)

    return sum(sumof)


if __name__ == '__main__':
    output = sum_diffs(sys.argv[1])
    print('Output: {}'.format(output))
