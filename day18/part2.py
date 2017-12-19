#!/usr/bin/python
import multiprocessing as mp
from queue import Empty
import sys


def add_to_dict(value, regs):
    if value.isalpha():
        if value not in regs:
            regs[value] = 0


def parse(p, list_of_strings, my_queue, other_queue, res_queue):
    regs = {}
    regs['p'] = p
    line_cntr = 0
    send_cnt = 0
    while True:
        try:
            line = list_of_strings[line_cntr]
        except IndexError:
            print('Line #: {} not in program'.format(line_cntr))
            res_queue.put(send_cnt)
            return
        vals = line.split()

        add_to_dict(vals[1], regs)
        try:
            add_to_dict(vals[2], regs)
        except IndexError:
            pass

        if vals[0] == 'snd':
            if vals[1] in regs:
                value = regs[vals[1]]
            else:
                value = int(vals[1])
            other_queue.put(value)
            send_cnt += 1
        elif vals[0] == 'set':
            if vals[2] in regs:
                value = regs[vals[2]]
            else:
                value = int(vals[2])
            regs[vals[1]] = value
        elif vals[0] == 'add':
            if vals[2] in regs:
                value = regs[vals[2]]
            else:
                value = int(vals[2])
            regs[vals[1]] += value
        elif vals[0] == 'mul':
            if vals[2] in regs:
                value = regs[vals[2]]
            else:
                value = int(vals[2])
            regs[vals[1]] *= value
        elif vals[0] == 'mod':
            if vals[2] in regs:
                value = regs[vals[2]]
            else:
                value = int(vals[2])
            regs[vals[1]] = regs[vals[1]] % value
        elif vals[0] == 'rcv':
            try:
                value = my_queue.get(timeout=5)
            except Empty:
                res_queue.put(send_cnt)
                return
            regs[vals[1]] = value
        elif vals[0] == 'jgz':
            if vals[1] in regs:
                value = regs[vals[1]]
            else:
                value = int(vals[1])
            if vals[2] in regs:
                jmp_value = regs[vals[2]]
            else:
                jmp_value = int(vals[2])
            if value > 0:
                line_cntr += (jmp_value - 1)
        line_cntr += 1


def name(list_of_strings):
    mp.set_start_method('spawn')
    q0 = mp.Queue()
    q1 = mp.Queue()
    res_q0 = mp.Queue()
    res_q1 = mp.Queue()
    p0 = mp.Process(target=parse, args=(0, list_of_strings, q0, q1, res_q0))
    p1 = mp.Process(target=parse, args=(1, list_of_strings, q1, q0, res_q1))
    p0.start()
    p1.start()

    p0.join()
    p1.join()

    r1 = res_q1.get()

    return r1


if __name__ == '__main__':
    # with open('example.txt') as f:
        # assert name([l.strip() for l in f.readlines()]) == 4

    with open(sys.argv[1]) as f:
        output = name([l.strip() for l in f.readlines()])
        print('Output: {}'.format(output))
