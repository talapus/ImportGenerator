#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
# import csv
import os
from time import time
from faker import Faker


def main():
    if len(sys.argv) <= 1:
        print ("Usage: gen # ")
    else:
        fake = Faker('bg_BG')
        dName = "import" + str(time())
        filename = "en_US.csv"
        if not os.path.exists(dName):
            os.makedirs(dName)
        with open("{0}/{1}".format(dName,filename), "wb") as output:
            # csvWriter = csv.writer(output)
            zlist = ["Unique ID", "First Name", "Last Name", "Email", "Registration Code",
                "Show on Attendee List", "Company Name", "Job Title", "Brief Bio",
                "Work Phone", "Mobile Phone", "Other Phone", "Other Phone Type",
                "Address", "Address 2", "City", "State", "Zipcode", "Country",
                "Website", "Website 2", "Linkedin URL", "Twitter URL", "Facebook URL",
                "Group List (comma-separated)"]
            print (zlist)
            # csvWriter.writerow(zlist)
            for i in range(0,int(sys.argv[1])):
                ylist = ["A-{0}".format(i), fake.first_name(), fake.last_name(),
                    fake.email(), " ", "FALSE", fake.word(), fake.slug(), fake.slug(),
                    fake.phone_number(), " ", " ", " ", " ", " ", fake.city(),
                    fake.slug(), fake.postcode(), fake.country(), fake.url(),
                    fake.url(), " ", " ", " ", " ", ]
                print (ylist)
                # csvWriter.writerow(ylist)
            print ("{0}/{1}").format(dName, filename)

if __name__ == '__main__':
    main()

'''

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

'''
