#!/usr/bin/env python

import string
import argparse
from sys import stdin


alphabet = string.ascii_lowercase


def shift(c, count):
    try:
        index = alphabet.index(c)
    except ValueError:
        return c

    new_index = (index + count) % len(alphabet)
    return alphabet[new_index]


def message_iterator(message):
    for m in message:
        if m not in string.ascii_letters:
            continue
        yield str.lower(m)


def crypt(message, count):
    if message is '-':
        message = stdin.read()

    return [shift(l, count) for l in message_iterator(message)]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('message', default='-')
    parser.add_argument('-c', '--count', type=int, default=1)
    args = parser.parse_args()

    new_message = ''.join(crypt(args.message, args.count))
    print(new_message)
