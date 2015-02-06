#!/usr/bin/env python

from faker import Faker
fake = Faker('zh_TW')

print fake.name()
