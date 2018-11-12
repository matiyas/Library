#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Poprawić zmienne globalne
#

import re
import os
import django
from urllib.request import urlopen
import lxml.html as lxhtml
from tqdm import tqdm


os.environ['DJANGO_SETTINGS_MODULE'] = 'LibSys.settings'
django.setup()

from BookBorrow.models import Book, Author, Language, Publishment, Subject


URL = 'https://bonito.pl'
CODING = 'iso-8859-2'
BOOK_DETAILS_XPATH = './/div[2]/div[1]/table/tr[2]/td[2]/table/tr/td/table'
BOOK_DETAILS_ROWS_XPATH = BOOK_DETAILS_XPATH + '/tr[1]/td/table[1]/tr[1]/td/table/tr/td[1]/span'
PAGES_PER_CATEGORY = 1
BOOKS_PER_PAGE = 15
LANG = Language.objects.get(name='Polish')


def clear_objects():
    Book.objects.all().delete()
    Author.objects.all().delete()
    Publishment.objects.all().delete()
    Subject.objects.all().delete()


def parse_rows(rows):
    authors_obj = []
    publishing_house_obj = year_obj = isbn_obj = None

    for row in rows:
        if re.match(r'Autor', str(row.xpath('td[1]')[0].text)):
            book_authors = [author.text for author in row.xpath('td[2]/table/tr/td/h2/a')]

            for author in book_authors:
                author_queryset = Author.objects.filter(name=author)

                if not author_queryset:
                    authors_obj.append(Author.objects.create(name=author))
                else:
                    authors_obj.append(author_queryset.first())

        if re.match(r'Wydawnictwo', str(row.xpath('td[1]')[0].text)):
            publishing_house = row.xpath('td[2]/a')[0].text
            publishing_house_queryset = Publishment.objects.filter(name=publishing_house)

            if not publishing_house_queryset:
                publishing_house_obj = Publishment.objects.create(name=publishing_house)
            else:
                publishing_house_obj = publishing_house_queryset.first()

        if re.match(r'Rok', str(row.xpath('td[1]')[0].text)):
            year_obj = row.xpath('td[2]/b')[0].text

        if re.match(r'Numer ISBN', str(row.xpath('td[1]')[0].text)):
            isbn_obj = row.xpath('td[2]/b')[0].text.replace('-', '')

    return {'authors': authors_obj, 'publishing_house': publishing_house_obj, 'year': year_obj, 'isbn': isbn_obj}


def parse_book(book_link, subject):
    book_html = urlopen(URL + book_link).read()
    book_tree = lxhtml.fromstring(book_html.decode(CODING))
    rows = book_tree.xpath(BOOK_DETAILS_ROWS_XPATH + '/span[1]/table/tr')
    title = book_tree.xpath(BOOK_DETAILS_ROWS_XPATH + '/h1/span')[0].text
    book_field = parse_rows(rows)
    new_book = Book.objects.create(
        title=title,
        isbn=book_field['isbn'],
        subject=subject,
        lang=LANG,
        publishment=book_field['publishing_house'],
        publication_year=book_field['year'],
    )

    for author in book_field['authors']:
        new_book.authors.add(author)

    # return title, book_field['isbn'], subject, LANG, book_field['publishing_house'], book_field['year']


def parse_page(page_link, subject):
    category_html = urlopen(URL + page_link).read()
    category_tree = lxhtml.fromstring(category_html)
    book_link_xpath = BOOK_DETAILS_XPATH + '/tr/td/table/tr[1]/td[1]/table/tr/td/a/@href'

    for index, book_link in enumerate(category_tree.xpath(book_link_xpath), 1):
        parse_book(book_link, subject)

    # with open('BookBorrow/fixtures/seed.yaml', 'w') as seed:
    #     for index, book_link in enumerate(category_tree.xpath(book_link_xpath), 1):
    #         book_fields = parse_book(book_link, subject)
    #         seed.write('- model: BookBorrow.Book\n')
    #         seed.write('\tpk: {}\n'.format(index))
    #         seed.write('\tfields:\n')
    #         seed.write('\t\ttitle: {}\n'.format(book_fields[0]))
    #         seed.write('\t\tisbn: {}\n'.format(book_fields[1]))
    #         seed.write('\t\tsubject: {}\n'.format(book_fields[2]))
    #         seed.write('\t\tlang: {}\n'.format(book_fields[3]))
    #         seed.write('\t\tpublishment: {}\n'.format(book_fields[4]))
    #         seed.write('\t\tpublication_year: {}\n'.format(book_fields[5]))

        PROGRESS_BAR.update(1)


def parse_category(category_link):
    subject = Subject.objects.create(name=category_link.text)
    link = category_link.xpath('@href')[0]

    for page in range(PAGES_PER_CATEGORY):
        link = link.split('-')
        link[2] = str(page)
        link = '-'.join(link)
        parse_page(link, subject)


def parse():
    html = urlopen(URL).read()
    tree = lxhtml.fromstring(html.decode(CODING))

    books_count_xpath = './/table[5]/tr[2]/td[2]/table/tr/td/table[1]/tr/td/div/div/font'
    books_count = len(tree.xpath(books_count_xpath)) * BOOKS_PER_PAGE * PAGES_PER_CATEGORY

    global PROGRESS_BAR
    PROGRESS_BAR = tqdm(total=books_count)

    for category in tree.xpath('.//table[5]/tr[2]/td[2]/table/tr/td/table[1]/tr/td/div/div/a'):
        parse_category(category)


if __name__ == '__main__':
    clear_objects()
    parse()
    PROGRESS_BAR.close()
