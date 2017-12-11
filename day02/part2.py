#!/usr/bin/python
import sys


def divides(row):
    for i, j in [[i, j] for i in row for j in row if i != j]:
        if i % j == 0:
            return i / j


def checksum(list_of_strings):
    rows = [list(map(lambda x: float(x), line.split())) for line in list_of_strings]

    return sum([divides(row) for row in rows])


if __name__ == '__main__':
    assert checksum(['5 9 2 8']) == 4
    assert checksum(['9 4 7 3']) == 3
    assert checksum(['3 8 6 5']) == 2
    assert checksum(['5 9 2 8', '9 4 7 3', '3 8 6 5']) == 9

    with open(sys.argv[1]) as f:
        output = checksum([l.strip() for l in f.readlines()])
        print('Output: {}'.format(output))
