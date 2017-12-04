#!/usr/bin/python
import sys


def check_dups(phrase):
    phrase_list = phrase.split(" ")

    for i in range(len(phrase_list)):
        if phrase_list[i] in phrase_list[i + 1:]:
            return True

    return False


def valid_passphrase(in_file):
    with open(in_file) as f:
        str_list = list(map(lambda x: x.strip(), f.readlines()))

        cnt = 0
        for phrase in str_list:
            if not check_dups(phrase):
                cnt += 1

    return cnt


if __name__ == '__main__':
    output = valid_passphrase(sys.argv[1])
    print('Output: {}'.format(output))
