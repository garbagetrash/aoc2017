#!/usr/bin/python
import sys


regs = {}
max_ever = 0


def parse_cond(cond, value, cond_reg):
    if cond == '>':
        if regs[cond_reg] > int(value):
            return True
        else:
            return False
    elif cond == '<':
        if regs[cond_reg] < int(value):
            return True
        else:
            return False
    elif cond == '>=':
        if regs[cond_reg] >= int(value):
            return True
        else:
            return False
    elif cond == '<=':
        if regs[cond_reg] <= int(value):
            return True
        else:
            return False
    elif cond == '==':
        if regs[cond_reg] == int(value):
            return True
        else:
            return False
    elif cond == '!=':
        if regs[cond_reg] != int(value):
            return True
        else:
            return False
    else:
        print('wat: {}, {}'.format(cond, value))
        return None


def parse_line(line):
    global max_ever  # WTFBBQ IS THIS SHIT
    words = line.split()

    cond_reg = words[4]
    reg = words[0]
    if cond_reg not in regs:
        regs[cond_reg] = 0
    if reg not in regs:
        regs[reg] = 0

    regs[cond_reg]
    cond = words[5]
    value = words[6]
    if parse_cond(cond, value, cond_reg):
        if words[1] == 'inc':
            regs[reg] += int(words[2])
        elif words[1] == 'dec':
            regs[reg] -= int(words[2])
        else:
            print('wtf')
        if regs[reg] > max_ever:
            max_ever = regs[reg]


def func1(in_file):
    with open(in_file) as f:
        str_list = list(map(lambda x: x.strip(), f.readlines()))

        for line in str_list:
            parse_line(line)


if __name__ == '__main__':
    output = func1(sys.argv[1])
    print('Output: {}'.format(max_ever))
