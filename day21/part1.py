#!/usr/bin/python3
import sys
import numpy as np


def to_matrix(string):
    rows = string.split('/')
    n_rows = len(rows)
    mat = np.ndarray((n_rows, n_rows), dtype=np.int32)
    for i, row in enumerate(rows):
        temp = []
        for c in row:
            if c == '.':
                temp.append(0)
            elif c == '#':
                temp.append(1)
        mat[i, :] = np.array(temp, dtype=np.int32)

    return mat


def to_string(mat):
    n_rows = len(mat)
    string = []
    for i in range(n_rows):
        for j in range(n_rows):
            if mat[i, j] == 0:
                string.append('.')
            elif mat[i, j] == 1:
                string.append('#')
        if i < n_rows - 1:
            string.append('/')

    return "".join(string)


def parse(list_of_strings):
    rules = {}
    for line in list_of_strings:
        vals = line.split()
        rules[vals[0]] = to_matrix(vals[2])

    return rules


def check_rotations(image, rule):
    check = rule
    for i in range(4):
        check = np.rot90(check)
        if np.array_equal(image, check):
            return True

    return False


def is_match(image, rule):
    check = rule
    if check_rotations(image, check):
        return True
    check = np.fliplr(check)
    if check_rotations(image, check):
        return True
    check = np.flipud(check)
    if check_rotations(image, check):
        return True

    return False


def test_is_match():
    test_input = '.#./..#/###'
    out = ['.#./#../###']
    out.append('###/..#/.#.')
    out.append('#../#.#/##.')
    out.append('#../###/##.')
    out.append('###/.##/.#.')
    out.append('.#./##./###')

    assert is_match(to_matrix(out[0]), to_matrix(test_input)) is True
    assert is_match(to_matrix(out[1]), to_matrix(test_input)) is True
    assert is_match(to_matrix(out[2]), to_matrix(test_input)) is True
    assert is_match(to_matrix(out[3]), to_matrix(test_input)) is False
    assert is_match(to_matrix(out[4]), to_matrix(test_input)) is False
    assert is_match(to_matrix(out[5]), to_matrix(test_input)) is False


def image_split(image):
    image_arr = []
    if len(image) % 2 == 0:
        side_len = len(image) // 2
        rows = np.split(image, side_len)
        for i in range(len(image) // 2):
            cols = np.split(rows[i], side_len, axis=1)
            for c in cols:
                image_arr.append(c)

    elif len(image) % 3 == 0:
        side_len = len(image) // 3
        rows = np.split(image, side_len)
        for i in range(len(image) // 3):
            cols = np.split(rows[i], side_len, axis=1)
            for c in cols:
                image_arr.append(c)

    else:
        raise ValueError('WTF')

    return image_arr


def test_image_split():
    """
    Tests: image_split, to_string, to_matrix
    """
    image = '#..#/..../..../#..#'
    assert [to_string(x) for x in image_split(to_matrix(image))] == ['#./..', '.#/..', '../#.', '../.#']


def reassemble_subs(new_subs):
    image = []
    side_len = int(np.sqrt(len(new_subs)))
    col_array = []
    for i in range(side_len):
        row_array = []
        for j in range(side_len):
            row_array.append(new_subs[side_len * i + j])

        row = np.concatenate(row_array, axis=0)
        col_array.append(row)

    image = np.concatenate(col_array, axis=1)

    return image


def iterate(image, rules):

    # Split image into sub-categories
    sub_images = image_split(to_matrix(image))

    # For each subcategory, run through rules
    new_subs = []
    for sub_image in sub_images:
        print('sub: {}'.format(sub_image))
        for rule in rules:
            if is_match(sub_image, to_matrix(rule)):
                new_subs.append(rules[rule])
                break

    print('new_subs: {}'.format(new_subs))
    # Reassemble sub tiles
    output = reassemble_subs(new_subs)

    print('output: {}'.format(output))
    return to_string(output)


def count_on_bits(image):
    return np.sum(to_matrix(image))


def name(list_of_strings, N):
    rules = parse(list_of_strings)

    image = '.#./..#/###'
    for i in range(N):
        image = iterate(image, rules)

    cnt = count_on_bits(image)
    return cnt


if __name__ == '__main__':
    test_is_match()
    test_image_split()
    assert name(['../.# => ##./#../...',
                 '.#./..#/### => #..#/..../..../#..#'], 2) == 12

    with open(sys.argv[1]) as f:
        output = name([l.strip() for l in f.readlines()], 5)
        print('Output: {}'.format(output))
