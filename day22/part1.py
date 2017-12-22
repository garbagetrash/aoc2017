#!/usr/bin/python
import sys


class World():

    def __init__(self, list_of_strings):
        self.dict = {}
        self.parse(list_of_strings)

    def parse(self, list_of_strings):
        mid = len(list_of_strings) // 2
        for i, line in enumerate(list_of_strings):
            for j, c in enumerate(line):
                if c == '#':
                    self.dict[(i - mid, j - mid)] = 1

    def get_state(self, row, col):
        if (row, col) not in self.dict:
            return 0
        else:
            return self.dict[(row, col)]

    def infect(self, row, col):
        self.dict[(row, col)] = 1

    def clean(self, row, col):
        self.dict[(row, col)] = 0


class Virus():

    def __init__(self):
        self.row = 0
        self.col = 0
        self.facing = 'u'
        self.num_infections = 0

    def turn(self, world):
        state = world.get_state(self.row, self.col)
        if state == 1:
            self.turn_right()
            world.clean(self.row, self.col)
        else:
            self.turn_left()
            world.infect(self.row, self.col)
            self.num_infections += 1

        self.move_forward()

    def turn_right(self):
        if self.facing == 'u':
            self.facing = 'r'
        elif self.facing == 'r':
            self.facing = 'd'
        elif self.facing == 'd':
            self.facing = 'l'
        elif self.facing == 'l':
            self.facing = 'u'

    def turn_left(self):
        if self.facing == 'u':
            self.facing = 'l'
        elif self.facing == 'r':
            self.facing = 'u'
        elif self.facing == 'd':
            self.facing = 'r'
        elif self.facing == 'l':
            self.facing = 'd'

    def move_forward(self):
        if self.facing == 'u':
            self.row -= 1
        elif self.facing == 'r':
            self.col += 1
        elif self.facing == 'd':
            self.row += 1
        elif self.facing == 'l':
            self.col -= 1


def name(list_of_strings, N=10000):
    world = World(list_of_strings)
    virus = Virus()

    for i in range(N):
        virus.turn(world)

    return virus.num_infections


if __name__ == '__main__':
    assert name(['..#', '#..', '...'], N=10000) == 5587

    with open(sys.argv[1]) as f:
        output = name([l.strip() for l in f.readlines()], N=10000)
        print('Output: {}'.format(output))
