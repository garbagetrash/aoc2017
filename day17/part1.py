#!/usr/bin/python
import sys


class CircBuf():

    def __init__(self):
        self.array = [0]
        self.idx = 0

    def step(self, nsteps):
        self.idx = (self.idx + nsteps) % len(self.array)
        # print(self.idx)

    def insert(self, val):
        self.array.insert(self.idx + 1, val)
        self.idx += 1
        if len(self.array) < 1:
            print(self.idx)
            print(self.array)


def name(input_string, N):
    cbuf = CircBuf()
    for i in range(N):
        cbuf.step(int(input_string))
        cbuf.insert(int(i) + 1)

    return cbuf.array[cbuf.idx + 1]


if __name__ == '__main__':
    assert name('3', 2017) == 638

    with open(sys.argv[1]) as f:
        output = name(f.read().strip(), 2017)
        print('Output: {}'.format(output))
