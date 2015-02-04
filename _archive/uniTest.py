#!/usr/bin/env python

from faker import Faker
fake = Faker('zh_TW')


chName = u"{}".format(fake.name())

print fake.name()
print type(chName)
