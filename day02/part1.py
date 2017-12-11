#!/usr/bin/python
import sys


def diff(line):
    row = list(map(lambda x: float(x), line.split()))
    return max(row) - min(row)


def checksum(list_of_strings):
    return sum([diff(line) for line in list_of_strings])


if __name__ == '__main__':
    assert checksum(['5 1 9 5']) == 8
    assert checksum(['7 5 3']) == 4
    assert checksum(['2 4 6 8']) == 6
    assert checksum(['5 1 9 5', '7 5 3', '2 4 6 8']) == 18

    with open(sys.argv[1]) as f:
        output = checksum([l.strip() for l in f.readlines()])
        print('Output: {}'.format(output))
