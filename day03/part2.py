#!/usr/bin/python
import sys


def add_offset(x, y, vals):
    try:
        return vals[(x, y)]
    except KeyError:
        return 0


def sum_of_neighbors(pos, vals):
    x1, y1 = pos
    offsets = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]]

    return sum([add_offset(x1 + x2, y1 + y2, vals) for x2, y2 in offsets])


def spiral_memory(input_value):
    vals = {}
    x = 0
    y = 0
    xlim = 1
    ylim = 1
    dx = 1
    dy = 0
    while True:
        if abs(dx) > 0 and abs(x) < xlim or abs(dy) > 0 and abs(y) < ylim:
            pass
        else:
            # change direction
            if dx > 0:
                dx = 0
                dy = 1
            elif dx < 0:
                dx = 0
                dy = -1
            elif dy > 0:
                dx = -1
                dy = 0
            else:
                dx = 1
                dy = 0
                xlim += 1
                ylim += 1
        pos = (x, y)
        if pos in vals:
            raise ValueError('Position {} should not already be in dictionary'.format(pos))
        if pos != (0, 0):
            vals[pos] = sum_of_neighbors(pos, vals)
        else:
            vals[pos] = 1

        if vals[pos] > input_value:
            return vals[pos]

        x += dx
        y += dy


if __name__ == '__main__':
    assert spiral_memory(0) == 1
    assert spiral_memory(1) == 2
    assert spiral_memory(2) == 4
    assert spiral_memory(4) == 5
    assert spiral_memory(5) == 10

    with open(sys.argv[1]) as f:
        output = spiral_memory(int(f.read().strip()))
        print('Output: {}'.format(output))
