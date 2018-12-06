#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, request, url_for

from text_sorter import remove_non_alnum, sort_ascending, divide_text
from crawl import crawl, remove_html_tag


app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main.html')


@app.route('/', methods=['POST'])
def print_result():
    if request.method == 'POST':
        url = request.form['url']
        input_type = request.form['type']
        output_unit = int(request.form['unit'])

        text = crawl(url)
        if input_type.upper() == 'HTML':
            text = remove_html_tag(text)

        text = remove_non_alnum(text)
        text = sort_ascending(text)
        shares, rest = divide_text(text, output_unit)

        return render_template('main.html', shares=shares, rest=rest)
    else:
        return redirect(url_for('main_page'))


if __name__ == '__main__':
    app.run()
