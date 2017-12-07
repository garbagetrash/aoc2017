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


def find_unbalanced_diff():
    # Find an unbalanced node
    temp = None
    for node in nodes:
        if not nodes[node].check_children_weights_balanced():
            temp = node
            break

    # Now find the problem child
    children = nodes[temp].children
    weights = list(map(lambda x: nodes[x].get_limb_weight(), nodes[temp].children))
    idx = find_unlike_idx(weights)

    # Now follow that childs problem children to the source
    while not nodes[children[idx]].check_children_weights_balanced():
        children = nodes[temp].children
        weights = list(map(lambda x: nodes[x].get_limb_weight(), nodes[temp].children))
        idx = find_unlike_idx(weights)

    # Now figure out what the source needed to be to conform
    diff = weights[idx] - weights[(idx - 1) % 3]
    return nodes[children[idx]].weight - diff


def find_unlike_idx(weights):
    a, b, c = weights
    if a == b:
        return 2
    elif a == c:
        return 1
    else:
        return 0


def parse_line(line):
    words = line.split()
    name = words[0]
    weight = words[1].lstrip('\(').rstrip('\)')
    children = list(map(lambda x: x.rstrip('\,'), words[3:]))
    nodes[name] = Node(name, children, weight)


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

    return find_unbalanced_diff()


if __name__ == '__main__':
    output = tower(sys.argv[1])
    print('Output: {}'.format(output))
