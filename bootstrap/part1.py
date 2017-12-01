#!/usr/bin/python
import sys


def func1(in_file):
    vals = []
    with open(in_file) as f:
        in_string = f.read().strip()
        for c in in_string:
            vals.append(int(c))

    return 0


if __name__ == '__main__':
    output = func1(sys.argv[1])
    print('Output: {}'.format(output))
