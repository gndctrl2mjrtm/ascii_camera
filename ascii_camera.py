#!/bin/env/python
# -*- encoding: utf-8 -*-
"""

"""
from __future__ import division, print_function

import os

import cv2


char_set = "$@B%8&WXMZO0QLCJUYX#*oahkbdpqwmzcvunxrjftIi1l!/\|(){}[]?-_+~<>;:," \
           "\"^'." + ":" * 10 + "." * 10 + "`" * 15 + " " * 50
char_set = list(char_set)
n_chars = len(char_set) - 1


def cvrt(n):
    return char_set[int((n / 255) * n_chars)]


def convert_frame(frame):
    output = ''
    for row in frame:
        output += ''.join(list(map(cvrt, row))) + '\n'
    return output


def _main():
    rows, columns = os.popen('stty size', 'r').read().split()
    rows, columns = int(int(rows) / 2), int(int(columns) / 2)

    print(rows, columns)

    test_path = '/Users/rosewang/Desktop/test_image.jpg'
    assert os.path.exists("/Users/rosewang/Desktop")
    assert os.path.exists(test_path)

    test_image = cv2.imread(test_path)
    test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
    h, w = test_image.shape[:2]

    print(h, w)

    # w*c h*c where c := scaling factor from column width
    # (height/column)*height

    new_w, new_h = columns, int((w / h) * columns)
    print(new_w, new_h)

    frame = cv2.resize(test_image, (new_h, new_w))

    print(convert_frame(frame))


def main():
    video_data = cv2.VideoCapture(0)

    while True:
        _, frame = video_data.read()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        h, w = frame.shape[:2]
        # w*c h*c where c := scaling factor from column width
        # (height/column)*height

        rows, columns = os.popen('stty size', 'r').read().split()
        rows, columns = int(int(rows)), int(int(columns))

        if rows < columns:
            new_w, new_h = int((w / h) * rows), rows
        else:
            new_w, new_h = columns, int((w / h) * columns)

        frame = cv2.resize(frame, (new_w, new_h))

        print(convert_frame(frame))
        print('\n' * (rows - new_w))


if __name__ == "__main__":
    main()
