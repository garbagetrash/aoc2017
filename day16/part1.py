#!/usr/bin/python
import sys


def parse(input_string, init_programs):
    programs = [c for c in init_programs]
    dance_seq = input_string.split(',')
    for seq in dance_seq:
        if seq[0] == 's':
            s = int(seq[1:])
            programs = programs[-s:] + programs[:-s]
        elif seq[0] == 'x':
            a, b = [int(c) for c in seq[1:].split('/')]
            temp = programs[a]
            programs[a] = programs[b]
            programs[b] = temp
        elif seq[0] == 'p':
            a, b = [c for c in seq[1:].split('/')]
            idxa = programs.index(a)
            idxb = programs.index(b)
            programs[idxa] = b
            programs[idxb] = a

    output = "".join(programs)
    return output


def permutation_promenade(input_string, init_programs):
    programs = parse(input_string, init_programs)
    return programs


if __name__ == '__main__':
    assert permutation_promenade('s1,x3/4,pe/b', 'abcde') == 'baedc'

    with open(sys.argv[1]) as f:
        output = permutation_promenade(f.read().strip(), 'abcdefghijklmnop')
        print('Output: {}'.format(output))
