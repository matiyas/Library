#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'LibSys.settings'
django.setup()

from BookBorrow.models import Language

response = requests.get('https://raw.githubusercontent.com/umpirsky/' +
                        'language-list/master/data/en_US/language.json')
langs = json.loads(response.text)

for code in langs.keys():
    Language.objects.create(code=code, name=langs[code])
