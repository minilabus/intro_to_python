#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Print all numbers of a Fibonacci sequence up to an upper limit.
"""

import sys


def fibonacci(max_val):
    """ Generate a list of number following a Fibonacci sequence up to a maximum value (max_val)  """
    max_val = float(max_val)

    if max_val < 1:
        raise ValueError('Only support positive integer, excluding 0!')

    seq = [1, 1]
    # The last one is always over the limit, so a pop() is required
    while seq[-1] <= max_val:
        seq.append(seq[-1] + seq[-2])

    if seq[-1] > 1:
        seq.pop(-1)

    return seq


def main():
    if len(sys.argv) > 2:
        raise IOError('This script only support 0 or 1 argument!')

    if len(sys.argv) > 1:
        max_val = sys.argv[1]
    else:
        max_val = input('What is the upper limit? ')

    fibo_seq = fibonacci(max_val)
    print('Fibonacci sequence (up to {}) is:'.format(max_val))
    print('\t', fibo_seq)


if __name__ == "__main__":
    main()
