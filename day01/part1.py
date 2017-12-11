#!/usr/bin/python
import sys
import numpy as np


def inverse_captcha(input_string):
    vals = np.array([int(c) for c in input_string])
    truth_arr = [vals[i] == vals[(i + 1) % len(vals)] for i in range(len(vals))]

    return sum(vals[truth_arr])


if __name__ == '__main__':
    assert inverse_captcha('1122') == 3
    assert inverse_captcha('1111') == 4
    assert inverse_captcha('1234') == 0
    assert inverse_captcha('91212129') == 9

    with open(sys.argv[1]) as f:
        output = inverse_captcha(f.read().strip())
        print('Output: {}'.format(output))
