#!/usr/bin/env python

import sys
from faker import Faker
fake = Faker()


def main():
    if len(sys.argv) <= 1:
        print "How many?"
    else:
        for i in range(0, int(sys.argv[1])):
            print (str(i) + " " + fake.name_male())


# main

if __name__ == '__main__':
        main()
