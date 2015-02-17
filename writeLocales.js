#!/usr/bin/env node

var fake = require('faker');
var fs = require('fs');

if (!process.argv[2] || isNaN(+process.argv[2])) {
  console.log("Gruh?");
} else { // only write a file if the user indicates how many records
  userInput = +process.argv[2];
  var stream = fs.createWriteStream("en_US.csv");
  stream.once('open', function(fd) {
    for (i=0; i<userInput; i++) {
      stream.write(fake.name.firstName() + "\n");
    }
    stream.end();
  });
}


console.log("en_US.csv");
