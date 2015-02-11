#!/usr/bin/env node

/*
 * A command line script to produce mocked data output for the
 * CrowdCompass CSV input interfaces.
 *
 * Usage: gsvGen [#]
*/

var fake = require('faker');
var fs = require('fs');

var URL = function() { return("http://www." + fake.internet.domainName() + "/" + fake.lorem.words(1)); };
var Company = function() { return(fake.company.bsAdjective() + " " + fake.company.bsNoun())};
var Job = function() { return(fake.company.catchPhraseAdjective() + " " + fake.company.catchPhraseNoun() + " Specialist") };

var locales = ['de', 'de_AT','de_CH','en','en_AU','en_BORK','en_CA','en_GB','en_IND',
  'en_US','en_au_ocker','es','fa','fr','it','ja','ko','nb_NO','nep','nl','pl','pt_BR',
  'ru','sk','sv','vi','zh_CN'];

if (!process.argv[2]) {
  console.log("Usage: csvGen #");
} else {
  input = +process.argv[2];
  console.log("Unique ID, First Name, Last Name, Email, Registration Code, Show on Attendee List, Company Name, Job Title, Brief Bio, Work Phone, Mobile Phone, Other Phone, Other Phone Type, Address, Address 2, City, State, Zipcode, Country, Website, Website 2, Linkedin URL, Twitter URL, Facebook URL, Group List (comma-separated)");
  for (var i=0; i < input; i++) {
      for (i=0; i < locales.length; i++) {
        fake.locale = locales[i];
        var stream = fs.createWriteStream(locales[i] + "_import.csv");
        stream.once('open', function(fd) {
          stream.write("A-" + (i+1) + ", " + fake.name.firstName() + ", " + fake.name.lastName()
               + ", " + fake.internet.email() + ", " + ", " + "FALSE, " + Company()
               + ", " + Job() + ", " + ", " + fake.phone.phoneNumber() + ", " + ", "
               + ", " + ", " + fake.address.streetAddress() + ", " + ", " + fake.address.city()
               + ", " + fake.address.state() + ", " + fake.address.zipCode()
               + ", " + fake.address.country() + ", " + URL() + ", " + URL()
               + ", " + ", " + ", " + ", ");
          stream.end();
      }
   }
}

/*

var stream = fs.createWriteStream("my_file.txt");
stream.once('open', function(fd) {
  stream.write("My first row\n");
  stream.write("My second row\n");
  stream.end();
});

console.log("File output as my_file.txt");

*/
