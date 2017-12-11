#!/usr/bin/python
import sys
import numpy as np


def inverse_captcha(input_string):
    vals = np.array([int(c) for c in input_string])
    halfway = int(len(vals) / 2)
    truth_arr = [vals[i] == vals[(i + halfway) % len(vals)] for i in range(len(vals))]

    return sum(vals[truth_arr])


if __name__ == '__main__':
    assert inverse_captcha('1212') == 6
    assert inverse_captcha('1221') == 0
    assert inverse_captcha('123425') == 4
    assert inverse_captcha('123123') == 12
    assert inverse_captcha('12131415') == 4

    with open(sys.argv[1]) as f:
        output = inverse_captcha(f.read().strip())
        print('Output: {}'.format(output))
