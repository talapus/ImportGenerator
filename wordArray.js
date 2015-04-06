#!/usr/bin/env node

var fake = require('faker');

var bigBio = function(input) {
  wordArray = [];

  for (var i=0; i<input; i++) {
    wordArray[i] = fake.hacker.noun();
  };
  console.log(wordArray + " ");
}

bigBio(3);
