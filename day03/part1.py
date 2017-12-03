#!/usr/bin/python


vals = {}


def find_dist(input_value):

    x = 0
    y = 0
    pos = (x, y)
    vals[pos] = 1
    xlim = 1
    ylim = 1
    dx = 1
    dy = 0
    cnt = 2
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
        vals[pos] = cnt
        cnt += 1

        if vals[pos] == input_value:
            print(abs(x) + abs(y))
            break


if __name__ == '__main__':
    find_dist(325489)
