#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import django
from urllib.request import urlopen
import lxml.html as lxhtml


os.environ['DJANGO_SETTINGS_MODULE'] = 'LibSys.settings'
django.setup()

from BookBorrow.models import Book, Author, Language, Publishment, Subject

url = 'https://bonito.pl'
html = urlopen(url).read()

tree = lxhtml.fromstring(html.decode('iso-8859-2'))
publishing_houses = set()
authors = set()
polish_lang = Language.objects.get(english_name='Polish')
book_authors = publishing_house = year = isbn = publishing_house_object = author_objects = None

for category in tree.xpath('/html/body/div[3]/div[2]/table[5]/tr[2]/td[2]/table/tr/td/table[1]/tr/td/div/div/a'):
    subject = Subject.objects.create(name=category.text)
    link = category.xpath('@href')[0]
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

        for row in rows:
            if re.match(r'Autor', str(row.xpath('td[1]')[0].text)):
                book_authors = [author.text for author in row.xpath('td[2]/table/tr/td/h2/a')]
                author_objects = []

                for author in book_authors:
                    if author not in authors:
                        author_split = author.split()
                        author_objects.append(
                            Author.objects.create(first_name=' '.join(author_split[:-1]), last_name=author_split[-1])
                        )
                        authors.add(author)

            if re.match(r'Wydawnictwo', str(row.xpath('td[1]')[0].text)):
                publishing_house = row.xpath('td[2]/a')[0].text

                if publishing_house not in publishing_houses:
                    print(publishing_house, publishing_houses)
                    publishing_house_object = Publishment.objects.create(name=publishing_house)
                    publishing_houses.add(publishing_house)

            if re.match(r'Rok', str(row.xpath('td[1]')[0].text)):
                year = row.xpath('td[2]/b')[0].text

            if re.match(r'Numer ISBN', str(row.xpath('td[1]')[0].text)):
                isbn = row.xpath('td[2]/b')[0].text.replace('-', '')

        new_book = Book.objects.create(
            title=title,
            isbn=isbn,
            subject=subject,
            lang=polish_lang,
            publishment=publishing_house_object,
            publication_year=year,
        )

        for author in author_objects:
            new_book.authors.add(author)
