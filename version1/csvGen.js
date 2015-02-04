#!/usr/bin/env node

/*
 * A command line script to produce mocked data output for the 
 * CrowdCompass CSV input interfaces.
 *
 * Usage:
 *  gsvGen [#] [attendees/organizations/etc.]
*/

// reqs

var fake = require('faker')
var clear = require('clear')

// funcdtions

var printURL = function() { return ("http://www." + fake.internet.domainName() + "/" + fake.lorem.words(1)); }

// main

if (!process.argv[2]) {
  console.log("Usage: csvGen # [a/o/etc.]");
} else {
  input = +process.argv[2];
  console.log("Unique ID", "First Name", "Last Name", "Email", "Registration Code",
                "Show on Attendee List", "Company Name", "Job Title", "Brief Bio",
                "Work Phone", "Mobile Phone", "Other Phone", "Other Phone Type",
                "Address", "Address 2", "City", "State", "Zipcode", "Country",
                "Website", "Website 2", "Linkedin URL", "Twitter URL", "Facebook URL",
                "Group List (comma-separated)")
  for (i=0; i < input; i++) {
    console.log("A-" + i + ", " + fake.name.firstName() + ", " + fake.name.lastName()
               + ", " + fake.internet.email() + ", " + ", " + fake.lorem.sentence()
               + ", " + "FALSE, " + fake.lorem.sentence() + ", " + fake.lorem.sentence()
               + ", " + fake.lorem.sentence() + ", " + fake.phone.phoneNumber()
               + ", " + ", " + ", " + ", " + ", " + fake.address.city()
               + ", " + fake.lorem.sentence() + ", " + fake.address.zipCode()
               + ", " + fake.address.country() + ", " + printURL() + ", " + printURL()
               + ", " + ", " + ", " + ", ");
  }
}

/*
                ylist = ["A-{0}".format(i), firstName, lastName,
                    email, " ", "FALSE", word, slug1, slug2,
                    phoneNumber, " ", " ", " ", " ", " ", city,
                    slug3, postCode, country, url1,
                    url2, " ", " ", " ", " ", ]
                csvWriter.writerow(ylist)
            print ("{0}/{1}").format(dName, filename)

if __name__ == '__main__':
    main()

'''

locales = ['bg_BG',
        'cs_CZ',
        'de_DE',
        'dk_DK',
        'el_GR',
        'en_CA',
        'en_GB',
        'en_US',
        'es_ES',
        'es_MX',
        'fa_IR',
        'fi_FI',
        'fr_FR',
        'hi_IN',
        'it_IT',
        'ko_KR',
        'lt_LT',
        'lv_LV',
        'nl_NL',
        'pl_PL',
        'pt_BR',
        'ru_RU',
        'sl_SI',
        'zh_CN',
        'zh_TW' ]

'''

*/

/*
 * ToDo:
 * [ ] Functional: output onto the command line for > filename.csv
 * [ ] Output files. Create a directory to contain them
 * [ ] Localization. Drop files named by locale into the folder
 */
