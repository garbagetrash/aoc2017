#!/usr/bin/python
import sys


def spiral_memory(input_value):

    vals = {}
    x = 0
    y = 0
    cnt = 1
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
        vals[pos] = cnt

        if vals[pos] == input_value:
            return abs(x) + abs(y)

        x += dx
        y += dy
        cnt += 1


if __name__ == '__main__':
    assert spiral_memory(1) == 0
    assert spiral_memory(12) == 3
    assert spiral_memory(23) == 2
    assert spiral_memory(1024) == 31

    with open(sys.argv[1]) as f:
        output = spiral_memory(int(f.read().strip()))
        print('Output: {}'.format(output))
