#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import requests


r_html_tag = re.compile(r'<[^>]+>')


def crawl(url):
    req = requests.get(url)
    if req.status_code != 200:
        raise Exception('')

    return req.text


def remove_html_tag(html):
    return r_html_tag.sub('', html)


def test():
    url = 'https://finance.naver.com'
    html = crawl(url)
    text = remove_html_tag(html)
    print(text)


def main():
    test()


if __name__ == '__main__':
    main()

