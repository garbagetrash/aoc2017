#!/usr/bin/python
import sys


def a_series_of_tubes(level):
    xmax = len(level[0])
    ymax = len(level)
    px = level[0].index('|')
    py = 0
    dx = 0
    dy = 1

    str_list = []
    lastpx = px
    lastpy = py
    cnt = 0
    while True:
        if px < 0 or px >= xmax or py < 0 or py >= ymax:
            break
        if level[py][px] == '|':
            px += dx
            py += dy
        elif level[py][px] == '-':
            px += dx
            py += dy
        elif level[py][px].isalpha():
            str_list.append(level[py][px])
            px += dx
            py += dy
        elif level[py][px] == '+':
            if dx != 0:
                if px + dx < xmax and px + dx > 0 and level[py][px + dx] != ' ':
                    px += dx
                elif py - 1 > 0 and (level[py - 1][px] == '|' or
                                     level[py - 1][px] == '+' or
                                     level[py - 1][px].isalpha()):
                    dy = -1
                    dx = 0
                    py += dy
                elif py + 1 < ymax and (level[py + 1][px] == '|' or
                                        level[py + 1][px] == '+' or
                                        level[py + 1][px].isalpha()):
                    dy = 1
                    dx = 0
                    py += dy
                else:
                    raise ValueError('WTF')
            elif dy != 0:
                if py + dy < ymax and py + dy > 0 and level[py + dy][px] != ' ':
                    py += dy
                elif px - 1 > 0 and (level[py][px - 1] == '-' or
                                     level[py][px - 1] == '+' or
                                     level[py][px - 1].isalpha()):
                    dy = 0
                    dx = -1
                    px += dx
                elif px + 1 < xmax and (level[py][px + 1] == '-' or
                                        level[py][px + 1] == '+' or
                                        level[py][px + 1].isalpha()):
                    dy = 0
                    dx = 1
                    px += dx
                else:
                    raise ValueError('WTF')

        if px == lastpx and py == lastpy:
            break
        else:
            cnt += 1
            lastpx = px
            lastpy = py

    return cnt


if __name__ == '__main__':
    with open('example.txt') as f:
        assert a_series_of_tubes([l.rstrip('\n') for l in f.readlines()]) == 38

    with open(sys.argv[1]) as f:
        output = a_series_of_tubes([l.rstrip('\n') for l in f.readlines()])
        print('Output: {}'.format(output))
