#!/usr/bin/python
import sys


def func1(arg):
    return 0


def count_digit_sums(in_file):
    vals = []
    with open(in_file) as f:
        in_string = f.read().strip()
        for c in in_string:
            vals.append(int(c))

    total_sum = 0
    for i in range(len(vals) - 1):
        if vals[i] == vals[i + 1]:
            total_sum += vals[i]

    if vals[-1] == vals[0]:
        total_sum += vals[-1]

    return total_sum


if __name__ == '__main__':
    total_sum = count_digit_sums(sys.argv[1])
    print('Total sum: {}'.format(total_sum))
