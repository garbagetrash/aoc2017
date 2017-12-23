#!/usr/bin/python3
import sys
import numpy as np


rot2dict = {}
rot3dict = {}


def to_matrix(string):
    rows = string.split('/')
    n_rows = len(rows)
    mat = np.ndarray((n_rows, n_rows), dtype=np.int8)
    for i, row in enumerate(rows):
        temp = []
        for c in row:
            if c == '.':
                temp.append(0)
            elif c == '#':
                temp.append(1)
        mat[i, :] = np.array(temp, dtype=np.int8)

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
        k = tuple(np.reshape(to_matrix(vals[0]), (1, -1)).flatten())
        rules[k] = to_matrix(vals[2])

    print('Parsed rules.')

    return rules


def make_rot_2_dict():
    global rot2dict
    for i in range(16):
        k = np.array([int(c) for c in '{:04b}'.format(i)])
        rot2dict[tuple(k)] = np.reshape(np.rot90(np.reshape(k, (2, 2))), (1, -1)).flatten()
    print('Created rot2 dictionary.')


def make_rot_3_dict():
    global rot3dict
    for i in range(512):
        k = np.array([int(c) for c in '{:09b}'.format(i)])
        rot3dict[tuple(k)] = np.reshape(np.rot90(np.reshape(k, (3, 3))), (1, -1)).flatten()
    print('Created rot3 dictionary.')


def check_rotations(image, rule):
    global rot2dict
    global rot3dict
    if image.ndim != 1:
        image = np.reshape(image, (1, -1)).flatten()
    if len(image) == 4:
        if len(rule) != 4:
            return False
        d = rot2dict
    elif len(image) == 9:
        if len(rule) != 9:
            return False
        d = rot3dict
    else:
        raise ValueError('Length not 4 or 9: {}'.format(image))

    check = rule
    for i in range(4):
        check = d[tuple(check)]
        if (check == image).all():
            return True

    return False


def is_match(image, rule):
    """
    image = 1d array
    rule = 1d array
    """
    if image.ndim != 1:
        image = np.reshape(image, (1, -1)).flatten()
    check = rule
    if len(check) == 4:
        size2d = (2, 2)
    elif len(check) == 9:
        size2d = (3, 3)
    else:
        raise ValueError('WTF')

    if check_rotations(image, check):
        return True
    check = np.reshape(np.fliplr(np.reshape(check, size2d)), (1, -1)).flatten()
    if check_rotations(image, check):
        return True
    check = np.reshape(np.flipud(np.reshape(check, size2d)), (1, -1)).flatten()
    if check_rotations(image, check):
        return True

    return False


def image_split(image):
    image_arr = []
    if image.ndim == 1:
        n = int(np.sqrt(len(image)))
        image = np.reshape(image, (n, n))

    if len(image) % 2 == 0:
        side_len = len(image) // 2
        if side_len == 1:
            return [image]
        rows = np.split(image, side_len)
        for i in range(len(image) // 2):
            cols = np.split(rows[i], side_len, axis=1)
            for c in cols:
                image_arr.append(np.reshape(c, (1, -1)).flatten())

    elif len(image) % 3 == 0:
        side_len = len(image) // 3
        if side_len == 1:
            return [image]
        rows = np.split(image, side_len)
        for i in range(len(image) // 3):
            cols = np.split(rows[i], side_len, axis=1)
            for c in cols:
                image_arr.append(np.reshape(c, (1, -1)).flatten())

    else:
        raise ValueError('WTF')

    if image_arr[0].ndim != 1:
        raise ValueError('WTF')

    return image_arr


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

    return np.reshape(image, (1, -1)).flatten()


def iterate(image, rules):

    # Split image into sub-categories
    sub_images = image_split(image)

    # For each subcategory, run through rules
    new_subs = []
    for sub_image in sub_images:
        for rule in rules:
            if is_match(sub_image, rule):
                new_subs.append(rules[rule])
                break

    # If no rules for this, then return None
    if len(new_subs) == 0:
        return None

    # Reassemble sub tiles
    output = reassemble_subs(new_subs)

    return output


def calc_f0(rules):
    count_dict = {}
    for i in range(2 ** 4):
        k = np.array([int(c) for c in '{:04b}'.format(i)])
        count_dict[tuple(k)] = np.sum(k)
    for i in range(2 ** 9):
        k = np.array([int(c) for c in '{:09b}'.format(i)])
        count_dict[tuple(k)] = np.sum(k)

    print('Initial count dictionary created.')
    return count_dict


def calc_fi(dictionary, rules):
    count_dict = {}
    for i in range(2 ** 4):
        k = np.array([int(c) for c in '{:04b}'.format(i)])
        image = np.reshape(k, (2, 2))
        cnt = 0
        out_image = iterate(image, rules)
        if out_image is None:
            continue
        if out_image.ndim != 1:
            out_image = np.reshape(out_image, (1, -1)).flatten()
        if len(out_image) != 9:
            raise ValueError('Should be 1d array: {}'.format(out_image))
        try:
            count_dict[tuple(k)] = dictionary[tuple(out_image)]
        except KeyError:
            pass

    for i in range(2 ** 9):
        k = np.array([int(c) for c in '{:09b}'.format(i)])
        in_image = np.reshape(k, (3, 3))
        cnt = 0
        out_image = iterate(in_image, rules)
        if out_image is None:
            continue
        out_sub_images = image_split(out_image)
        for sub_image in out_sub_images:
            if sub_image.ndim != 1:
                sub_image = np.reshape(sub_image, (1, -1)).flatten()
            if len(sub_image) != 4:
                raise ValueError('Should be 1d array: {}'.format(sub_image))
            cnt += dictionary[tuple(sub_image)]
        count_dict[tuple(k)] = cnt

    print('Count dictionary created.')
    return count_dict


def name(list_of_strings, N):
    global rot2dict
    global rot3dict
    if len(rot2dict) == 0:
        make_rot_2_dict()
    if len(rot3dict) == 0:
        make_rot_3_dict()
    rules = parse(list_of_strings)

    dictionary = calc_f0(rules)
    for k in dictionary:
        if dictionary[k] != 0:
            print(dictionary[k], k)
    for i in range(N):
        print('Iteration {}:'.format(i))
        dictionary = calc_fi(dictionary, rules)
        for k in dictionary:
            if dictionary[k] != 0:
                print(dictionary[k], k)

    image = to_matrix('.#./..#/###')
    cnt = dictionary[tuple(np.reshape(image, (1, -1)).flatten())]
    print('Final:')
    for k in dictionary:
        if dictionary[k] != 0:
            print(dictionary[k], k)
    print('Count: {}'.format(cnt))
    return cnt


def doit(in_string):
    with open(in_string) as f:
        output = name([l.strip() for l in f.readlines()], 5)
        print('Output: {}'.format(output))


if __name__ == '__main__':
    assert name(['../.# => ##./#../...', '.#./..#/### => #..#/..../..../#..#'], 2) == 12

    with open(sys.argv[1]) as f:
        output = name([l.strip() for l in f.readlines()], 5)
        print('Output: {}'.format(output))
