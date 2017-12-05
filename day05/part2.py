#!/usr/bin/python
import sys


def jumps(in_file):
    with open(in_file) as f:
        instr_list = list(map(lambda x: int(x.strip()), f.readlines()))

        idx = 0
        cnt = 0
        while True:
            try:
                temp = instr_list[idx]
                last = idx
                idx += temp
                if temp >= 3:
                    instr_list[last] -= 1
                else:
                    instr_list[last] += 1
                cnt += 1
            except IndexError:
                return cnt


if __name__ == '__main__':
    output = jumps(sys.argv[1])
    print('Output: {}'.format(output))
