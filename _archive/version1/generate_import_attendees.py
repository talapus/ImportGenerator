#!/usr/bin/env python

import sys
from faker import Faker


def main():

    if len(sys.argv) <= 1:
        print "Please indicate the number of invitees"
    # elif sys.argv[2]:
    #    gen = Faker(str(sys.argv[2])
    #    print "Unique ID,First Name,Last Name,Email,Registration Code,Show on Attendee List,Company Name,Job Title,Brief Bio,Work Phone,Mobile Phone,Other Phone,Other Phone Type,Address,Address 2,City,State,Zipcode,Country,Website,Website 2,Linkedin URL,Twitter URL,Facebook URL,Group List (comma-separated)"
    else:
        gen = Faker()
        print "Unique ID,First Name,Last Name,Email,Registration Code,Show on Attendee List,Company Name,Job Title,Brief Bio,Work Phone,Mobile Phone,Other Phone,Other Phone Type,Address,Address 2,City,State,Zipcode,Country,Website,Website 2,Linkedin URL,Twitter URL,Facebook URL,Group List (comma-separated)"
        for i in range(0, int(sys.argv[1])):
            print "A-" + str(i+1) + ", " + gen.first_name() + ", " + gen.last_name() + ", " + gen.email() + ", " + " " + \
                ", " + "FALSE" + ", " + gen.word() + ", " + gen.slug() + ", " + gen.bs() + ", " + \
                gen.phone_number() + ", " + " " + ", " + " " + ", " + " " + ", " +\
                " " + ", " + " " + ", " + gen.city() + ", " + gen.state() + ", " + gen.postcode() + ", " +\
                gen.country() + ", " + gen.url() + ", " + gen.url() + ", " + " " + ", " + " " + ", " + " " + ", " + " "


'''
To Do:

[X]    Reformat into correct idomatic python coding style __main__

[ ]    function-alize the script. Make a function for the output ("def output", for instance),
        one that handles language, one that handles the command line interface.

[ ]    Add file handling. The python CSV library seems like an ideal place to start.

[ ]    Localization

    * [bg_BG](http://fake-factory.readthedocs.org/en/master/locales/bg_BG.html)
    * [cs_CZ](http://fake-factory.readthedocs.org/en/master/locales/cs_CZ.html)
    * [de_DE](http://fake-factory.readthedocs.org/en/master/locales/de_DE.html)
    * [dk_DK](http://fake-factory.readthedocs.org/en/master/locales/dk_DK.html)
    * [el_GR](http://fake-factory.readthedocs.org/en/master/locales/el_GR.html)
    * [en_CA](http://fake-factory.readthedocs.org/en/master/locales/en_CA.html)
    * [en_GB](http://fake-factory.readthedocs.org/en/master/locales/en_GB.html)
    * [en_US](http://fake-factory.readthedocs.org/en/master/locales/en_US.html)
    * [es_ES](http://fake-factory.readthedocs.org/en/master/locales/es_ES.html)
    * [es_MX](http://fake-factory.readthedocs.org/en/master/locales/es_MX.html)
    * [fa_IR](http://fake-factory.readthedocs.org/en/master/locales/fa_IR.html)
    * [fi_FI](http://fake-factory.readthedocs.org/en/master/locales/fi_FI.html)
    * [fr_FR](http://fake-factory.readthedocs.org/en/master/locales/fr_FR.html)
    * [hi_IN](http://fake-factory.readthedocs.org/en/master/locales/hi_IN.html)
    * [it_IT](http://fake-factory.readthedocs.org/en/master/locales/it_IT.html)
    * [ko_KR](http://fake-factory.readthedocs.org/en/master/locales/ko_KR.html)
    * [lt_LT](http://fake-factory.readthedocs.org/en/master/locales/lt_LT.html)
    * [lv_LV](http://fake-factory.readthedocs.org/en/master/locales/lv_LV.html)
    * [nl_NL](http://fake-factory.readthedocs.org/en/master/locales/nl_NL.html)
    * [pl_PL](http://fake-factory.readthedocs.org/en/master/locales/pl_PL.html)
    * [pt_BR](http://fake-factory.readthedocs.org/en/master/locales/pt_BR.html)
    * [ru_RU](http://fake-factory.readthedocs.org/en/master/locales/ru_RU.html)
    * [sl_SI](http://fake-factory.readthedocs.org/en/master/locales/sl_SI.html)
    * [zh_CN](http://fake-factory.readthedocs.org/en/master/locales/zh_CN.html)
    * [zh_TW](http://fake-factory.readthedocs.org/en/master/locales/zh_TW.html)
'''



if __name__ == '__main__':
        main()
