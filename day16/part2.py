#!/usr/bin/python
from numba import jit, int32
import numpy as np
import sys


def compile_instructions(input_string):
    instr = []
    dance_seq = input_string.split(',')
    for seq in dance_seq:
        if seq[0] == 's':
            instr.append(0)
            s = int(seq[1:])
            instr.append(s)
        elif seq[0] == 'x':
            instr.append(1)
            a, b = [int(c) for c in seq[1:].split('/')]
            instr.append(a)
            instr.append(b)
        elif seq[0] == 'p':
            instr.append(2)
            a, b = [ord(c) - ord('a') for c in seq[1:].split('/')]
            instr.append(a)
            instr.append(b)

    return np.array(instr, dtype=np.int32)


@jit(int32[:, :](int32[:, :], int32))
def spin(mat, s):
    temp = mat[:, -s:].copy()
    mat[:, s:] = mat[:, :-s]
    mat[:, :s] = temp
    return mat


# Operates on indexes (a, b)
@jit(int32[:, :](int32[:, :], int32, int32))
def exchange(mat, a, b):
    temp = mat[:, a].copy()
    mat[:, a] = mat[:, b]
    mat[:, b] = temp
    return mat


# Operates on programs (a, b)
@jit(int32[:, :](int32[:, :], int32, int32))
def partner(mat, a, b):
    temp = mat[a, :].copy()
    mat[a, :] = mat[b, :]
    mat[b, :] = temp
    return mat


@jit(int32[:, :](int32[:], int32[:, :]))
def run(instr, mat):
    idx = 0
    len_instr = len(instr)
    while idx < len_instr:
        if instr[idx] == 0:
            s = instr[idx + 1]
            mat = spin(mat, s)
            idx += 2
        elif instr[idx] == 1:
            a = instr[idx + 1]
            b = instr[idx + 2]
            mat = exchange(mat, a, b)
            idx += 3
        elif instr[idx] == 2:
            a = instr[idx + 1]
            b = instr[idx + 2]
            mat = partner(mat, a, b)
            idx += 3

    return mat


def permutation_promenade(input_string, init_programs, N):
    instr = compile_instructions(input_string)
    mat = np.eye(len(init_programs), dtype=np.int32)
    start_eye = mat.copy()

    cnt = 0
    states = [mat]
    while cnt < N:
        mat = run(instr, mat)
        states.append(mat.copy())
        cnt += 1
        if np.array_equal(mat, start_eye):
            cycle_freq = cnt
            n_iters = N % cycle_freq
            mat = states[n_iters]
            break

    output = []
    for i in range(len(mat)):
        output.append(np.argmax(mat[:, i]))
    output = "".join([chr(c + ord('a')) for c in output])
    return output


if __name__ == '__main__':
    assert permutation_promenade('s1,x3/4,pe/b', 'abcde', 1) == 'baedc'
    assert permutation_promenade('s1,x3/4,pe/b', 'abcde', 2) == 'ceadb'

    with open(sys.argv[1]) as f:
        assert permutation_promenade(f.read().strip(), 'abcdefghijklmnop', 1) == 'ebjpfdgmihonackl'
    with open(sys.argv[1]) as f:
        output = permutation_promenade(f.read().strip(), 'abcdefghijklmnop', 100)
        print('Output: {}'.format(output))
