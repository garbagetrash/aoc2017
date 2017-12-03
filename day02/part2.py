#!/usr/bin/python
import sys


def sum_divs(in_file):
    sumof = []
    with open(in_file) as f:
        str_list = list(map(lambda x: x.strip(), f.readlines()))
        for s in str_list:
            line = list(map(lambda x: float(x), s.split()))
            for i in range(len(line)):
                for j in range(len(line)):
                    if line[i] % line[j] == 0 and i != j:
                        sumof.append(line[i] / line[j])

    return sum(sumof)


if __name__ == '__main__':
    output = sum_divs(sys.argv[1])
    print('Output: {}'.format(output))
