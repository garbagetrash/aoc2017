#!/usr/bin/python
import sys


regs = {}


def parse_cond(cond, value, cond_reg):
    return eval(''.join(str(regs[cond_reg]) + cond + value))


def parse_line(line):
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


def func1(in_file):
    with open(in_file) as f:
        str_list = list(map(lambda x: x.strip(), f.readlines()))

        for line in str_list:
            parse_line(line)

    values = [v for v in regs.values()]
    return max(values)


if __name__ == '__main__':
    output = func1(sys.argv[1])
    print('Output: {}'.format(output))
