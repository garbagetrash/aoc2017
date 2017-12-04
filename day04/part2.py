#!/usr/bin/python
import sys


def check_anagram(phrase):
    phrase_list = phrase.split(" ")

    for i in range(len(phrase_list)):
        word = phrase_list[i]
        wl = [c for c in word]
        wl.sort()
        for w2 in phrase_list[(i + 1):]:
            w2l = [c for c in w2]
            w2l.sort()
            if wl == w2l:
                return True

    return False


def valid_passphrase(in_file):
    with open(in_file) as f:
        str_list = list(map(lambda x: x.strip(), f.readlines()))

        cnt = 0
        for phrase in str_list:
            if not check_anagram(phrase):
                cnt += 1

    return cnt


if __name__ == '__main__':
    output = valid_passphrase(sys.argv[1])
    print('Output: {}'.format(output))
