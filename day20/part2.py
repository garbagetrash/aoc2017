#!/usr/bin/python3
import re
import sys
import numpy as np


def add_particle(line):
    m = re.split('[a-zA-Z<>=, ]+', line)
    m = [int(s) for s in m if s != '']
    pos = np.array([m[0], m[1], m[2]], dtype=np.int32)
    vel = np.array([m[3], m[4], m[5]], dtype=np.int32)
    acc = np.array([m[6], m[7], m[8]], dtype=np.int32)
    return (pos, vel, acc)


def step(pos, vel, acc):
    vel += acc
    pos += vel
    return (pos, vel, acc)


def time_n(particle, n=1):
    acc = particle[2]
    vel = particle[1]
    pos = particle[0]
    vel = acc * n + vel
    pos = acc * n * n + vel * n + pos
    return (pos, vel, acc)


def remove_collisions(particles):
    positions = {}
    collision_idx = []
    for i, p in enumerate(particles):
        pos = (p[0][0], p[0][1], p[0][2])
        if pos in positions:
            print('collision')
            collision_idx.append(i)
            collision_idx.append(positions[pos])
        else:
            positions[pos] = i

    collision_idx = list(set(collision_idx))
    collision_idx.reverse()

    for i in collision_idx:
        del particles[i]

    return particles


def done_yet(particles):
    dist = []
    accs = []
    for i, p in enumerate(particles):
        mann_dist = sum([abs(x) for x in p[0]])
        mann_accs = sum([abs(x) for x in p[2]])
        accs.append((mann_accs, i))
        dist.append((mann_dist, i))

    dist.sort()
    accs.sort()
    particle_idxs_a = [x[1] for x in accs]
    particle_idxs_p = [x[1] for x in dist]
    print(accs[:10])
    print(particle_idxs_a[:10])
    print(particle_idxs_p[:10])

    return particle_idxs_a == particle_idxs_p


def test(list_of_strings):
    particles = []
    for line in list_of_strings:
        particles.append(add_particle(line))

    N = 10000000
    for p in particles:
        time_n(p, N)

    print(done_yet(particles))


def name(list_of_strings):
    particles = []
    for line in list_of_strings:
        particles.append(add_particle(line))

    done = False
    cnt = 0
    while not done:
        for i, p in enumerate(particles):
            particles[i] = step(p[0], p[1], p[2])
        particles = remove_collisions(particles)

        if cnt % 100 == 0:
            print(cnt, len(particles))

        done = done_yet(particles)
        cnt += 1

        if cnt > 200:
            break

    return len(particles)


def doit(input_string):
    with open(input_string) as f:
        output = name([l.strip() for l in f.readlines()])
        print('Output: {}'.format(output))


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        output = name([l.strip() for l in f.readlines()])
        print('Output: {}'.format(output))
