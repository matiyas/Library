#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'LibSys.settings'
django.setup()

from BookBorrow.models import Language


response_en = requests.get('https://raw.githubusercontent.com/umpirsky/'+
                     'language-list/master/data/en_US/language.json')
response_pl = requests.get('https://raw.githubusercontent.com/umpirsky/'+
                     'language-list/master/data/pl_PL/language.json')
langs_en = json.loads(response_en.text)
langs_pl = json.loads(response_pl.text)

for code in langs_en.keys():
    language = Language(code=code, english_name=langs_en[code], polish_name=langs_pl[code])
    language.save()
