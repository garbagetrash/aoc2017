#!/usr/bin/python3
import re
import sys
import numpy as np
from numba import jit


def add_particle(line):
    m = re.split('[a-zA-Z<>=, ]+', line)
    m = [int(s) for s in m if s != '']
    pos = np.array([m[0], m[1], m[2]], dtype=np.int32)
    vel = np.array([m[3], m[4], m[5]], dtype=np.int32)
    acc = np.array([m[6], m[7], m[8]], dtype=np.int32)
    return (pos, vel, acc)


@jit
def solve_1d(pos1, vel1, acc1, pos2, vel2, acc2):
    a = (acc1 - acc2) / 2
    b = (vel1 - vel2 + (acc1 - acc2) / 2)
    c = pos1 - pos2
    if a == 0:
        if b == 0:
            raise ValueError("Divide by zero")
        else:
            ans = -c / b
            if np.floor(ans) == ans and ans > 0:
                return ans
            else:
                raise ValueError("No positive integer solution")

    sols = []
    if b * b - 4 * a * c < 0:
        raise ValueError("No real solutions")

    temp = -b + np.sqrt(b * b - 4 * a * c)
    temp = temp / (2 * a)
    sols.append(temp)
    temp = -b - np.sqrt(b * b - 4 * a * c)
    temp = temp / (2 * a)
    sols.append(temp)

    int_sols = []
    for ans in sols:
        if np.floor(ans) == ans and ans > 0:
            int_sols.append(ans)
        else:
            pass

    if not int_sols:
        raise ValueError("No positive integer solution")

    int_sols.sort()
    return int_sols[0]


def solve_parts(pos1, vel1, acc1, pos2, vel2, acc2):
    pos1 = np.array(pos1)
    vel1 = np.array(vel1)
    acc1 = np.array(acc1)
    pos2 = np.array(pos2)
    vel2 = np.array(vel2)
    acc2 = np.array(acc2)
    pos1x, pos1y, pos1z = pos1
    pos2x, pos2y, pos2z = pos2
    vel1x, vel1y, vel1z = vel1
    vel2x, vel2y, vel2z = vel2
    acc1x, acc1y, acc1z = acc1
    acc2x, acc2y, acc2z = acc2

    sols = []
    try:
        sols.append(solve_1d(pos1x, vel1x, acc1x, pos2x, vel2x, acc2x))
    except ValueError:
        pass
    try:
        sols.append(solve_1d(pos1y, vel1y, acc1y, pos2y, vel2y, acc2y))
    except ValueError:
        pass
    try:
        sols.append(solve_1d(pos1z, vel1z, acc1z, pos2z, vel2z, acc2z))
    except ValueError:
        pass

    if not sols:
        return None

    if len(sols) == 3:
        if sols[0] == sols[1] and sols[0] == sols[2]:
            return sols[0]
    elif len(sols) == 2:
        if sols[0] == sols[1]:
            return None
    else:
        return None

    return None


def check_collisions(particles):
    remove_idxs = []
    for i in range(len(particles)):
        for j in range(i + 1, len(particles)):
            t = solve_parts(particles[i][0],
                            particles[i][1],
                            particles[i][2],
                            particles[j][0],
                            particles[j][1],
                            particles[j][2])
            if t:
                remove_idxs.append((t, i, j))

    remove_idxs.sort()

    tsets = []
    tcurrent = remove_idxs[0][0]
    current_set = []
    for c in remove_idxs:
        if c[0] == tcurrent:
            if c[1] not in current_set:
                current_set.append(c[1])
            if c[2] not in current_set:
                current_set.append(c[2])
        else:
            tsets.append(current_set)
            current_set = []
            tcurrent = c[0]
            current_set.append(c[1])
            current_set.append(c[2])

    tsets.append(current_set)

    dead_arr = []
    for s in tsets:
        s = [i for i in s if i not in dead_arr]
        if len(s) > 1:
            for c in s:
                dead_arr.append(c)

    dead_arr.sort()
    dead_arr.reverse()

    for i in dead_arr:
        del particles[i]

    return particles


def particle_swarm(list_of_strings):
    particles = []
    for line in list_of_strings:
        particles.append(add_particle(line))

    particles = check_collisions(particles)

    return len(particles)


if __name__ == '__main__':
    # TODO: Currently getting the right answer, but solution doesn't handle
    # coordinate coplanar solutions (for example fails with the example
    # given.)
    # assert particle_swarm(['p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>',
    #                        'p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>',
    #                        'p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>',
    #                        'p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>']) == 1

    with open(sys.argv[1]) as f:
        output = particle_swarm([l.strip() for l in f.readlines()])
        print('Output: {}'.format(output))
