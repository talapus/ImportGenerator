#!/usr/bin/env python

import time
import sys

ztime = time.ctime()

if len(sys.argv) <= 1:
    print "Please enter a word"
else:
    print "\n\t{0}".format(sys.argv[1])
    print (ztime)
