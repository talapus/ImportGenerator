#!/usr/bin/env python

from faker import Faker
import os

fake = Faker()
dName = fake.postalcode_plus4()


if not os.path.exists(dName):
    os.makedirs(dName)


print "{} created", dName
