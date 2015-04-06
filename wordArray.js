#!/usr/bin/env node

var fake = require('faker');

var bigBio = function(input) {
  wordArray = [];
  console.log("wordArray before loop: " + wordArray);

  for (var i=0; i<input; i++) {
    wordArray[i] = fake.hacker.noun();
  };
  console.log("wordArray after loop: " + wordArray);
}

bigBio(3);
