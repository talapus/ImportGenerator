#!/usr/bin/env node

var fake = require('faker');
var fs = require('fs');
//var localeKey = ["en_US", "en_AU", "en_UK"];
var localeKey = "en_US";  // lets just go with English for now and make it functional

if (!process.argv[2] || isNaN(+process.argv[2])) {
  console.log("Usage: csvGen #");
} else { // only write a file if the user indicates how many records
  userInput = +process.argv[2];
  var stream = fs.createWriteStream("en_US.csv");
  stream.once('open', function(fd) {
    stream.write("Record, First Name, Last Name, Email \n");
    for (i=0; i<userInput; i++) {
      stream.write(fake.name.firstName() + ", " + fake.name.lastName() + ", " + fake.internet.email() + "\n");
    }
    stream.end();
    console.log(localeKey + ".csv created");
  });
}
