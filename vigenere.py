#!/usr/bin/env python

import argparse
import itertools
from caesar import alphabet


def shift(c, k):
    pad = alphabet.index(k)
    try:
        index = alphabet.index(c)
    except ValueError:
        return c

    new_index = (index + pad) % len(alphabet)
    return alphabet[new_index]


def key_iterator(key):
    for i in itertools.count():
        yield key[i % len(key)]


def crypt(message, key):
    return [shift(m, k) for m, k in zip(message, key_iterator(key))]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('message')
    parser.add_argument('-k', '--key', type=str)
    args = parser.parse_args()

    new_message = ''.join(crypt(args.message, args.key))
    print(new_message)
