#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv
import os
from time import time
from faker import Faker


def main():
    if len(sys.argv) <= 1:
        print ("Usage: gen # ")
    else:
        locale = 'zh_TW'
        fake = Faker(locale)
        dName = "import" + str(time())
        filename = locale + ".csv"
        if not os.path.exists(dName):
            os.makedirs(dName)
        with open("{0}/{1}".format(dName,filename), "wb") as output:
            csvWriter = csv.writer(output)
            zlist = ["Unique ID", "First Name", "Last Name", "Email", "Registration Code",
                "Show on Attendee List", "Company Name", "Job Title", "Brief Bio",
                "Work Phone", "Mobile Phone", "Other Phone", "Other Phone Type",
                "Address", "Address 2", "City", "State", "Zipcode", "Country",
                "Website", "Website 2", "Linkedin URL", "Twitter URL", "Facebook URL",
                "Group List (comma-separated)"]
            csvWriter.writerow(zlist)
            for i in range(0,int(sys.argv[1])):
                firstName = u'{}'.format(fake.first_name())
                lastName = u'{}'.format(fake.last_name())
                email = u'{}'.format(fake.email())
                word = u'{}'.format(fake.word())
                slug1 = u'{}'.format(fake.slug())
                slug2 = u'{}'.format(fake.slug())
                phoneNumber = u'{}'.format(fake.phone_number())
                city = u'{}'.format(fake.city())
                slug3 = u'{}'.format(fake.slug())
                postCode = u'{}'.format(fake.postcode())
                country = u'{}'.format(fake.country())
                url1 = u'{}'.format(fake.url())
                url2 = u'{}'.format(fake.url())
                ylist = ["A-{0}".format(i), firstName, lastName,
                    email, " ", "FALSE", word, slug1, slug2,
                    phoneNumber, " ", " ", " ", " ", " ", city,
                    slug3, postCode, country, url1,
                    url2, " ", " ", " ", " ", ]
                csvWriter.writerow(ylist)
            print ("{0}/{1}").format(dName, filename)

if __name__ == '__main__':
    main()

'''

locales = ['bg_BG',
        'cs_CZ',
        'de_DE',
        'dk_DK',
        'el_GR',
        'en_CA',
        'en_GB',
        'en_US',
        'es_ES',
        'es_MX',
        'fa_IR',
        'fi_FI',
        'fr_FR',
        'hi_IN',
        'it_IT',
        'ko_KR',
        'lt_LT',
        'lv_LV',
        'nl_NL',
        'pl_PL',
        'pt_BR',
        'ru_RU',
        'sl_SI',
        'zh_CN',
        'zh_TW' ]

'''
