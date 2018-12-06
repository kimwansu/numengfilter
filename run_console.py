#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

from text_sorter import remove_non_alnum, sort_ascending, divide_text
from crawl import crawl, remove_html_tag


r_non_digit = re.compile(r'[^0-9]+')


def main():
    url = input('URL: ')
    if not url:
        print('URL이 입력되지 않았습니다.')
        return

    input_type = input('1-TXT, 2-HTML: ')
    if input_type not in ['1', '2']:
        print('잘못된 입력 타입')
        return

    output_unit = input('출력 묶음 단위(자연수): ')
    if r_non_digit.findall(output_unit):
        print('자연수가 아닌 값 입력')
        return

    output_unit = int(output_unit)

    text = crawl(url)
    if input_type == '2':
        text = remove_html_tag(text)

    text = remove_non_alnum(text)
    text = sort_ascending(text)
    shares, rest = divide_text(text, output_unit)

    print('몫: ', ', '.join(shares))
    print('나머지: ', rest)


if __name__ == '__main__':
    main()

