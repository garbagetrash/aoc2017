#!/usr/bin/python
from numba import jit
import sys
import numpy as np


class CircBuf():

    def __init__(self):
        self.array = np.zeros(50000001)
        self.idx = 0
        self.len = 1

    def step(self, nsteps):
        self.idx = (self.idx + nsteps) % self.len

    def insert(self, val):
        self.array[self.idx + 1] = val
        self.idx += 1
        self.len += 1


def name(input_string, N):
    cbuf = CircBuf()
    step = int(input_string)
    for i in range(N):
        if i % 100000 == 0:
            print(i)
        cbuf.step(step)
        cbuf.insert(int(i) + 1)

    return cbuf.array[1]


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        output = name(f.read().strip(), 5000000)
        print('Output: {}'.format(output))
