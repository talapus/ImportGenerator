#!/usr/bin/env python

import sys


def getInput():
    if len(sys.argv) <= 1:
        print "Argument required"

def displayOutput():
    print "\n\t{0}".format(sys.argv[1])

def main():
    getInput()
    displayOutput()


if __name__ == '__main__':
        main()
