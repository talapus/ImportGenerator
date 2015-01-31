import sys
from faker import Faker

gen = Faker()

# command-line interface

if len(sys.argv) <= 1:
    print "Please indicate the number of invitees"
else:
    print "Name, Username, Email"
    for i in range(0, int(sys.argv[1])):
        print gen.name() + ", " + gen.user_name() + ", " + gen.email()


'''
The following snippet ca be used to write a file, but I might just
leave this alone and require the
file redirector to create an output file.

----
with open("file.txt", "w") as my_file:
    my_file.write("Success!")
'''
