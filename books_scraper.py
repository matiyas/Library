#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import django
from urllib.request import urlopen
from bs4 import BeautifulSoup
import lxml.html as lxhtml


os.environ['DJANGO_SETTINGS_MODULE'] = 'LibSys.settings'
django.setup()

from BookBorrow.models import Book

url = 'https://bonito.pl'
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tree = lxhtml.fromstring(html)
publishing_houses = set()
authors = set()

for link in tree.xpath('/html/body/div[3]/div[2]/table[5]/tr[2]/td[2]/table/tr/td/table[1]/tr/td/div/div/a/@href'):
    category_html = urlopen(url + link).read()
    category_tree = lxhtml.fromstring(category_html)

    for book_link in category_tree.xpath('/html/body/div[2]/div[1]/table/tr[2]/td[2]/table/tr/td/table/tr/td/table/'
                                         'tr[1]/td[1]/table/tr/td/a/@href'):
        book_html = urlopen(url + book_link).read()
        book_tree = lxhtml.fromstring(book_html.decode('iso-8859-2'))
        rows = book_tree.xpath('/html/body/div[2]/div[1]/table[2]/tr[2]/td[2]/table/tr/td/table/tr[1]/td/table[1]/'
                               'tr[1]/td/table/tr/td[1]/span/span[1]/table/tr')
        title = book_tree.xpath('/html/body/div[2]/div[1]/table[2]/tr[2]/td[2]/table/tr/td/table/tr[1]/td/table[1]/'
                                'tr[1]/td/table/tr/td[1]/span/h1/span')[0].text

        book_authors = publishing_house = year = isbn = None

        for row in rows:
            if re.match(r'Autor', str(row.xpath('td[1]')[0].text)):
                book_authors = [author.text for author in row.xpath('td[2]/table/tr/td/h2/a')]
                authors |= set(book_authors)
            if re.match(r'Wydawnictwo', str(row.xpath('td[1]')[0].text)):
                publishing_house = row.xpath('td[2]/a')[0].text
                publishing_houses.add(publishing_house)
            if re.match(r'Rok', str(row.xpath('td[1]')[0].text)):
                year = row.xpath('td[2]/b')[0].text
            if re.match(r'Numer ISBN', str(row.xpath('td[1]')[0].text)):
                isbn = row.xpath('td[2]/b')[0].text.replace('-', '')

        print('Name:', title)
        print('Author:', book_authors)
        print('Publishment:', publishing_house)
        print('Year:', year)
        print('ISBN:', isbn)
        print()
