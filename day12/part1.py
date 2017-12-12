#!/usr/bin/python
import sys


class Node():

    def __init__(self, id_num):
        self.id_num = id_num
        self.edges = []

    def add_edge(self, edge):
        if edge not in self.edges:
            self.edges.append(edge)


class Graph():

    def __init__(self):
        self.nodes = {}

    def connect(self, a, b):
        if a not in self.nodes:
            self.nodes[a] = Node(a)
        if b not in self.nodes:
            self.nodes[b] = Node(b)
        self.nodes[a].add_edge(b)
        self.nodes[b].add_edge(a)

    def get_group(self, seed_id):
        group = []
        to_check = [seed_id]
        while len(to_check) > 0:
            id_num = to_check[0]
            if id_num not in group:
                group.append(id_num)
                to_check += [j for j in self.nodes[id_num].edges if j not in group]
            to_check.remove(id_num)

        return group


def create_graph(list_of_strings):
    graph = Graph()
    for line in list_of_strings:
        row = [x.rstrip(',') for x in line.split()]
        lhs = int(row[0])
        rhs = [int(x) for x in row[2:]]
        for r in rhs:
            graph.connect(lhs, r)

    return graph


def digital_plumber(list_of_strings):
    graph = create_graph(list_of_strings)

    return len(graph.get_group(0))


if __name__ == '__main__':
    assert digital_plumber(['0 <-> 2',
                            '1 <-> 1',
                            '2 <-> 0, 3, 4',
                            '3 <-> 2, 4',
                            '4 <-> 2, 3, 6',
                            '5 <-> 6',
                            '6 <-> 4, 5']) == 6

    with open(sys.argv[1]) as f:
        output = digital_plumber([l.strip() for l in f.readlines()])
        print('Output: {}'.format(output))
