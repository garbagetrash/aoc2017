#!/usr/bin/python
import sys


def add_to_dict(value, regs):
    if value.isalpha():
        if value not in regs:
            regs[value] = 0


def parse(list_of_strings, regs):
    line_cntr = 0
    mul_times = 0
    while True:
        try:
            line = list_of_strings[line_cntr]
        except IndexError:
            return mul_times
        vals = line.split()

        add_to_dict(vals[1], regs)
        try:
            add_to_dict(vals[2], regs)
        except IndexError:
            pass

        if vals[0] == 'set':
            if vals[2] in regs:
                value = regs[vals[2]]
            else:
                value = int(vals[2])
            regs[vals[1]] = value
        elif vals[0] == 'sub':
            if vals[2] in regs:
                value = regs[vals[2]]
            else:
                value = int(vals[2])
            regs[vals[1]] -= value
        elif vals[0] == 'mul':
            if vals[2] in regs:
                value = regs[vals[2]]
            else:
                value = int(vals[2])
            mul_times += 1
            regs[vals[1]] *= value
        elif vals[0] == 'jnz':
            if vals[1] in regs:
                value = regs[vals[1]]
            else:
                value = int(vals[1])
            if vals[2] in regs:
                jmp_value = regs[vals[2]]
            else:
                jmp_value = int(vals[2])
            if value != 0:
                line_cntr += (jmp_value - 1)
        line_cntr += 1

    return mul_times


def name(list_of_strings):
    regs = {}
    mul_times = parse(list_of_strings, regs)

    return mul_times


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        output = name([l.strip() for l in f.readlines()])
        print('Output: {}'.format(output))
