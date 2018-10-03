#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import django
from urllib.request import urlopen
from bs4 import BeautifulSoup

os.environ['DJANGO_SETTINGS_MODULE'] = 'LibSys.settings'
django.setup()

from BookBorrow.models import Country


html = urlopen('https://pl.wikipedia.org/wiki/ISO_3166-1').read()
soup = BeautifulSoup(html.decode('utf-8'), 'html.parser')

countries = []
for link in soup.find_all('a', href=re.compile(r'/wiki/ISO_3166-1_alfa-2#[A-Z]{2}')):
	row = link.parent.parent.find_all('td')
	country = Country(
		code=row[2].string, 
		english_name=row[1].string, 
		polish_name=row[0].a.string
	)
	country.save()
	
