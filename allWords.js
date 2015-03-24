#!/usr/bin/env node

var fake = require('faker');

var showUsage = function() {
  console.log("Usage");
}

if (!process.argv[2] || isNaN(+process.argv[2])) {
  showUsage();
} else {
  numWords = +process.argv[2];
  var allWords = fake.lorem.words(numWords);
  for (var i=0; i<allWords.length; i++) {
    console.log(allWords[i]);
  };
}
