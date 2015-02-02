#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, sys
from faker import Faker

fake = Faker()

'''
 update_progress() : Displays or updates a console progress bar
 Accepts a float between 0 and 1. Any int will be converted to a float.
 A value under 0 represents a 'halt'.
 A value at 1 or bigger represents 100%
'''


def update_progress(progress):
    barLength = 20  # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = u"\r{0} {1}% {2}".format("#" *block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()


# update_progress test script

locales = ['bg_BG',\
        'cs_CZ',\
        'de_DE',\
        'dk_DK',\
        'el_GR',\
        'en_CA',\
        'en_GB',\
        'en_US',\
        'es_ES',\
        'es_MX',\
        'fa_IR',\
        'fi_FI',\
        'fr_FR',\
        'hi_IN',\
        'it_IT',\
        'ko_KR',\
        'lt_LT',\
        'lv_LV',\
#       'ne_NP',\   # Broken?
        'nl_NL',\
#       'no_NO',\   # Broken?
        'pl_PL',\
        'pt_BR',\
#       'pt_PT',\   # Broken?
        'ru_RU',\
        'sl_SI',\
#       'tr_TR',\   # Broken?
        'zh_CN',\
        'zh_TW' ]

for e in locales:
    fake = Faker(e)
    for i in range(100):
        time.sleep(0.01)
        update_progress(i/100.0)
    print e, fake.name(), fake.city()

print ""
