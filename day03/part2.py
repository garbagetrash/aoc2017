#!/usr/bin/python


vals = {}


def add_offset(x, y):
    try:
        return vals[(x, y)]
    except KeyError:
        return 0


def sum_of_neighbors(pos):
    total = 0
    total += add_offset(pos[0] - 1, pos[1] - 1)
    total += add_offset(pos[0], pos[1] - 1)
    total += add_offset(pos[0] + 1, pos[1] - 1)
    total += add_offset(pos[0] - 1, pos[1])
    total += add_offset(pos[0] + 1, pos[1])
    total += add_offset(pos[0] - 1, pos[1] + 1)
    total += add_offset(pos[0], pos[1] + 1)
    total += add_offset(pos[0] + 1, pos[1] + 1)

    return total


def find_first(input_value):

    x = 0
    y = 0
    pos = (x, y)
    vals[pos] = 1
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
        x += dx
        y += dy
        pos = (x, y)
        if pos in vals:
            raise ValueError
        vals[pos] = sum_of_neighbors(pos)

        if vals[pos] > input_value:
            print(vals[pos])
            break


if __name__ == '__main__':
    find_first(325489)
