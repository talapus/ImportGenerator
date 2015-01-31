#!/usr/bin/env python

import sys
import csv
from faker import Faker


def main():
    if len(sys.argv) <= 1:
        print "Usage: gen # "
    else:
        fake = Faker()
        filename = str(fake.md5()) + ".csv"
        with open(filename, "wb") as output:
            csvWriter = csv.writer(output)
            zlist = ["Unique ID", "First Name", "Last Name", "Email", "Registration Code",\
                "Show on Attendee List", "Company Name", "Job Title", "Brief Bio",\
                "Work Phone", "Mobile Phone", "Other Phone", "Other Phone Type",\
                "Address", "Address 2", "City", "State", "Zipcode", "Country",\
                "Website", "Website 2", "Linkedin URL", "Twitter URL", "Facebook URL",\
                "Group List (comma-separated)"]
            csvWriter.writerow(zlist)
            for i in range(0,int(sys.argv[1])):
                ylist = ["A-{0}".format(i), fake.first_name(), fake.last_name(),\
                    fake.email(), " ", "FALSE", fake.word(), fake.slug(), fake.bs(),\
                    fake.phone_number(), " ", " ", " ", " ", " ", fake.city(),
                    fake.state(), fake.postcode(), fake.country(), fake.url(),\
                    fake.url(), " ", " ", " ", " ", ]
                csvWriter.writerow(ylist)
            print "File output as ", filename

if __name__ == '__main__':
    main()

