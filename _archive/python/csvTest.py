#!/usr/bin/env python

import csv
from faker import Faker


def main():
    fake = Faker()
    with open("testfile.csv", "wb") as output:
        csvWriter = csv.writer(output)
        zlist = ["number", "first, name", "last name" , "email"]
        csvWriter.writerow(zlist)
        for i in range(0,10):
            ylist = ["A-{0}".format(i), fake.first_name(), fake.last_name(), fake.email()]
            csvWriter.writerow(ylist)

if __name__ == '__main__':
    main()

