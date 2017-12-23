#!/usr/bin/python3
from numba import jit


# determine if b is prime
@jit
def is_prime(b):
    for d in range(2, b):
        if b % d == 0:
            return False

    return True


b = 106500
cnt = 0
while b <= 123500:
    if not is_prime(b):
        cnt += 1
    b += 17

print('Output: {}'.format(cnt))
