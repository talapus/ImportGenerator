#  from faker import Factory
#  fake = Factory.create()

from faker import Faker
fake = Faker()

print fake.name()
print fake.timezone() + "\n"

print fake.email()
print fake.phone_number()
print fake.address()
print str(fake.latitude()) + ", " + str(fake.longitude()) + "\n"

print fake.slug()
print fake.ipv4()
print fake.ipv6()
print fake.md5()
print fake.sha1()
print fake.sha256() + "\n"

print fake.iso8601()
print str(fake.unix_time()) + "\n"
