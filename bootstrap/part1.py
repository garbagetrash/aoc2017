#!/usr/bin/python
import sys


def func1(in_file):
    with open(in_file) as f:
        in_string = f.read().strip()
        # str_list = list(map(lambda x: x.strip(), f.readlines()))

    return in_string


if __name__ == '__main__':
    output = func1(sys.argv[1])
    print('Output: {}'.format(output))
