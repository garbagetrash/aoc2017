#!/usr/bin/python
import sys


def parse_move(move, pos):
    if move == 'ne':
        offset = [1, 0, -1]
    elif move == 'se':
        offset = [1, -1, 0]
    elif move == 'nw':
        offset = [-1, 1, 0]
    elif move == 'sw':
        offset = [-1, 0, 1]
    elif move == 'n':
        offset = [0, 1, -1]
    elif move == 's':
        offset = [0, -1, 1]

    return [x + y for x, y in zip(pos, offset)]


def dist(pos):
    return float(sum([abs(x) for x in pos])) / 2.0


def hex_ed(directions):
    cube_pos = [0, 0, 0]
    for move in directions.split(','):
        cube_pos = parse_move(move, cube_pos)

    return dist(cube_pos)


if __name__ == '__main__':
    assert hex_ed('ne,ne,ne') == 3.0
    assert hex_ed('ne,ne,sw,sw') == 0.0
    assert hex_ed('ne,ne,s,s') == 2.0
    assert hex_ed('se,sw,se,sw,sw') == 3.0

    with open(sys.argv[1]) as f:
        output = hex_ed(f.read().strip())
        print('Output: {}'.format(output))
