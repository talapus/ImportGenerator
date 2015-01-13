import sys
from faker import Faker

gen = Faker()

# command-line interface

print "fix the attendee Unique IDs with an iterator"

'''
if len(sys.argv) <= 1:
    print "Please indicate the number of invitees"
else:
    print "Unique ID, Emails, Attendee Unique IDs, Name, Description, Start Time, End Time, Location Name"
    for i in range(0, int(sys.argv[1])):
        print "A-" + str(i+1) + ", " + gen.email() + ", " + "U-" + str(i+1) + ", " + gen.name() + ", " + gen.slug() + \
                ", " + ", " + ", " + gen.bs()
'''
