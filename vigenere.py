#!/usr/bin/env python

import string
import argparse
import itertools
from sys import stdin


alphabet = string.ascii_lowercase


def shift(c, k):
    pad = alphabet.index(k)
    try:
        index = alphabet.index(c)
    except ValueError:
        return c

    new_index = (index + pad) % len(alphabet)
    return alphabet[new_index]


def message_iterator(message):
    for m in message:
        if m not in string.ascii_letters:
            continue
        yield str.lower(m)


def key_iterator(key):
    for i in itertools.count():
        yield key[i % len(key)]


def crypt(message, key):
    if message is '-':
        message = stdin.read()

    return [shift(m, k) for m, k in zip(
        message_iterator(message), key_iterator(key))]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('message', default='-')
    parser.add_argument('-k', '--key', type=str)
    args = parser.parse_args()

    new_message = ''.join(crypt(args.message, args.key))
    print(new_message)
