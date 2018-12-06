#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


r_alnum = re.compile(r'[A-Za-z0-9]+')
r_alpha = re.compile(r'[A-Za-z]+')
r_digit = re.compile(r'[0-9]+')


def remove_non_alnum(text):
    return ''.join(r_alnum.findall(text))


def join_in_rotation(a, b):
    result = []
    l = min(len(a), len(b))
    for i in range(l):
        result.append('{}{}'.format(a[i], b[i]))

    result.append(a[l:])
    result.append(b[l:])

    return ''.join(result)


def order(ch):
    if ch.isupper():
        return ord(ch) * 2
    elif ch.islower():
        return ord(ch.upper()) * 2 + 1
    else:
        return ord(ch)


def sort_text(text):
    buf = list(text)
    buf.sort(key=lambda ch: order(ch))
    return ''.join(buf)


def sort_ascending(text):
    # isalpha()는 한글도 True를 반환하므로 정규표현식을 사용한다.
    alphas = ''.join(r_alpha.findall(text))
    alphas = sort_text(alphas)

    digits = ''.join(r_digit.findall(text))
    digits = sort_text(digits)

    return join_in_rotation(alphas, digits)


def divide_text(text, divisor):
    shares = []
    rest = text
    while len(rest) >= divisor:
        shares.append(rest[:divisor])
        rest = rest[divisor:]

    return (shares, rest)


def test():
    text = '!$0aabbA798!'
    text = remove_non_alnum(text)
    text = sort_ascending(text)
    shares, rest = divide_text(text, 4)
    print('몫: ', ', '.join(shares))
    print('나머지: ', rest)


def main():
    test()


if __name__ == '__main__':
    main()
