#!/usr/bin/env node

var fake = require('faker');
var fs = require('fs');

// var locales = ['de', 'de_AT','de_CH','en','en_AU','en_BORK','en_CA','en_GB','en_IND','en_US','en_au_ocker','es','fa','fr','it','ja','ko','nb_NO','nep','nl','pl','pt_BR','ru','sk','sv','vi','zh_CN'];
var locale = "en_US";  // lets just go with English for now and make it functional
var URL = function() { return("http://www." + fake.internet.domainName() + "/" + fake.lorem.words(1)); };
var Company = function() { return(fake.company.bsAdjective() + " " + fake.company.bsNoun())};
var Job = function() { return(fake.company.catchPhraseAdjective() + " " + fake.company.catchPhraseNoun() + " Specialist") };

var loopCheck = true;

if (!process.argv[2] || isNaN(+process.argv[2])) {
  console.log("Usage: csvGen #");

} else { // only write a file if the user indicates how many records
  userInput = +process.argv[2];
  var stream = fs.createWriteStream("en_US.csv");

  stream.once('open', function(fd) {
    stream.write("Unique ID, First Name, Last Name, Email, Registration Code, Show on Attendee List, Company Name, Job Title, Brief Bio, Work Phone, Mobile Phone, Other Phone, Other Phone Type, Address, Address 2, City, State, Zipcode, Country, Website, Website 2, Linkedin URL, Twitter URL, Facebook URL, Group List (comma-separated)\n");

    //for (z=0; z<locale.length; z++) { //. this loop causes it to fail. 

      for (i=0; i<userInput; i++) {
        stream.write("A-" + (i+1) + ", " + fake.name.firstName() + ", " + fake.name.lastName() + ", " + fake.internet.email() + ", " + ", " + "FALSE, " + Company() + ", " + Job() + ", " + ", " + fake.phone.phoneNumber() + ", " + ", " + ", " + ", " + fake.address.streetAddress() + ", " + ", " + fake.address.city() + ", " + fake.address.state() + ", " + fake.address.zipCode() + ", " + fake.address.country() + ", " + URL() + ", " + URL() + ", " + ", " + ", " + ", \n");
      }
      stream.end();
      console.log(locale + ".csv created");
    //}
  });
}
