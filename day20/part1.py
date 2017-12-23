#!/usr/bin/python
import re
import sys


class Vec3():

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Particle():

    def __init__(self, pos, vel, acc):
        self.pos = pos
        self.vel = vel
        self.acc = acc


def mann_dist(particle):
    return abs(particle.acc.x) + abs(particle.acc.y) + abs(particle.acc.z)


def add_particle(line):
    m = re.split('[a-zA-Z<>=, ]+', line)
    m = [int(s) for s in m if s != '']
    pos = Vec3(m[0], m[1], m[2])
    vel = Vec3(m[3], m[4], m[5])
    acc = Vec3(m[6], m[7], m[8])
    return Particle(pos, vel, acc)


def name(list_of_strings):
    particles = []
    for line in list_of_strings:
        particles.append(add_particle(line))

    min_dist = mann_dist(particles[0])
    min_idx = 0
    for i, p in enumerate(particles):
        value = mann_dist(p)
        if value < min_dist:
            min_dist = value
            min_idx = i

    return min_idx


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        output = name([l.strip() for l in f.readlines()])
        print('Output: {}'.format(output))
