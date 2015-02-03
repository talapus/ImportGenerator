import sys
from faker import Faker

if len(sys.argv) <= 1:
    print "Usage: gen #"
else:
    gen = Faker()
    print "Unique ID,First Name,Last Name,Email,Registration Code,Show on Attendee List,Company Name,Job Title,Brief Bio,Work Phone,Mobile Phone,Other Phone,Other Phone Type,Address,Address 2,City,State,Zipcode,Country,Website,Website 2,Linkedin URL,Twitter URL,Facebook URL,Group List (comma-separated)"
    for i in range(0, int(sys.argv[1])):
        print "A-" + str(i+1) + ", " + gen.first_name()  + ", " + gen.last_name() + ", " + gen.email() + ", " + " " + \
                ", " + "FALSE"  + ", " + gen.word() + ", " + gen.slug() + ", " + gen.bs() + ", " + \
                gen.phone_number() + ", " + " " + ", " + " " + ", " + " "  + ", " +\
                " " + ", " + " " + ", " + gen.city() + ", " + gen.state() + ", " + gen.postcode() + ", " +\
                gen.country() + ", " + gen.url() + ", " + gen.url() + ", " + " "  + ", " + " "  + ", " + " "  + ", " + " "
