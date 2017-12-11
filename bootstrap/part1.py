#!/usr/bin/python
import sys


def name(input_string):

    return False


if __name__ == '__main__':
    assert name('input_string') is False

    with open(sys.argv[1]) as f:
        output = name(f.read().strip())
        # output = name([l.strip() for l in f.readlines()])
        print('Output: {}'.format(output))
