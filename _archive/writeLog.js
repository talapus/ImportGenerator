#!/usr/bin/env node


var fs = require('fs');
var stream = fs.createWriteStream("my_file.txt");
stream.once('open', function(fd) {
  stream.write("My first row\n");
  stream.write("My second row\n");
  stream.end();
});

console.log("Generated: my_file.txt");
