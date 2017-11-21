#!/usr/bin/env python

import argparse


alphabet = 'abcdefghijklmnopqrstuvwxyz'


def shift(c, count):
    try:
        index = alphabet.index(c)
    except ValueError:
        return c

    new_index = (index + count) % len(alphabet)
    return alphabet[new_index]


def crypt(message, count):
    return [shift(l, count) for l in message]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('message')
    parser.add_argument('-c', '--count', type=int, default=1)
    args = parser.parse_args()

    new_message = ''.join(crypt(args.message, args.count))
    print(new_message)
