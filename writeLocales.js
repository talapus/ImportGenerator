#!/usr/bin/env node

var fake = require('faker');
var fs = require('fs');

var stream = fs.createWriteStream("my_file.txt");
myName = fake.name.firstName();
stream.once('open', function(fd) {
  stream.write(fake.name.firstName());
  // stream.write("My second row\n");
  stream.end();
});

console.log("File output as my_file.txt");
