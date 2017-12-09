#!/usr/bin/python
import sys


def func1(in_file):
    with open(in_file) as f:
        in_string = f.read().strip()

        pt_value = 0
        sum_value = 0
        garbage = False
        ignore = False
        cnt = 0
        for i, c in enumerate(in_string):
            if ignore:
                ignore = False
                pass
            else:
                if garbage and not ignore and c != '!' and c != '>':
                    cnt += 1
                if c == '{' and not garbage and not ignore:
                    pt_value += 1
                    sum_value += pt_value
                elif c == '}' and not garbage and not ignore:
                    pt_value -= 1
                elif c == '<' and not garbage and not ignore:
                    garbage = True
                elif c == '>' and not ignore:
                    garbage = False
                elif c == '!' and not ignore:
                    ignore = True

    return cnt


if __name__ == '__main__':
    output = func1(sys.argv[1])
    print('Output: {}'.format(output))
