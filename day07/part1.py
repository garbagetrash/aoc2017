#!/usr/bin/python
import sys


nodes = {}


class Node():
    children = []
    parent = None
    weight = None

    def __init__(self, name, children, weight):
        self.name = name
        self.children = children
        self.weight = int(weight)

    def check_children_weights_balanced(self):
        weights = []
        for child in self.children:
            weights.append(nodes[child].get_limb_weight())
        if len(set(weights)) <= 1:
            return True
        else:
            return False

    def get_limb_weight(self):
        s = 0
        for child in self.children:
            s += nodes[child].get_limb_weight()
        return self.weight + s


def parse_line(line):
    words = line.split()
    name = words[0]
    weight = words[1].lstrip('\(').rstrip('\)')
    children = list(map(lambda x: x.rstrip('\,'), words[3:]))
    nodes[name] = Node(name, children, weight)


def find_bottom():
    for node in nodes:
        if nodes[node].parent is None:
            return nodes[node].name


def set_parents():
    for node in nodes:
        for child in nodes[node].children:
            nodes[child].parent = nodes[node].name


def tower(in_file):
    with open(in_file) as f:
        str_list = list(map(lambda x: x.strip(), f.readlines()))

        for line in str_list:
            parse_line(line)

        set_parents()

    return find_bottom()


if __name__ == '__main__':
    output = tower(sys.argv[1])
    print('Output: {}'.format(output))
