#!/usr/bin/env python

import sys
from faker import Faker


def main():

    if len(sys.argv) <= 1:
        print "How many?"
    else:
        gen = Faker()
        print "Unique ID,First Name,Last Name,Email,Registration Code,Show on Attendee List,Company Name,Job Title,Brief Bio,Work Phone,Mobile Phone,Other Phone,Other Phone Type,Address,Address 2,City,State,Zipcode,Country,Website,Website 2,Linkedin URL,Twitter URL,Facebook URL,Group List (comma-separated)"
        for i in range(0, int(sys.argv[1])):
            print "A-" + str(i+1) + ", " + gen.first_name() + ", " + gen.last_name() + ", " + gen.email() + ", " + " " + \
                ", " + "FALSE" + ", " + gen.word() + ", " + gen.slug() + ", " + gen.bs() + ", " + \
                gen.phone_number() + ", " + " " + ", " + " " + ", " + " " + ", " +\
                " " + ", " + " " + ", " + gen.city() + ", " + gen.state() + ", " + gen.postcode() + ", " +\
                gen.country() + ", " + gen.url() + ", " + gen.url() + ", " + " " + ", " + " " + ", " + " " + ", " + " "


if __name__ == '__main__':
        main()


'''

Notes/Qs:
    1. How to breakup the long print line while retaining required output (no extra whitespace)
    2. Should this be further functionalized? Simple is better...
    3. How to loop my "for i in range" into a list
    4. Then output the list f.write(str(item): "\n")



Some file IO examples:

---- with open as file ----
with open("file.txt", "w") as my_file:
    my_file.write("Success!")


-----------------

my_list = [i**2 for i in range(1,11)]

f = open("output.txt", "w")

for item in my_list:
    f.write(str(item) + "\n")

f.close()

'''
