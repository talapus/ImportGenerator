#!/usr/bin/env node

var fake = require('faker');

var randomBio = function(input) {
  wordArray = [];

  var bioSize = function() {
    return (Math.floor(Math.random() * 1500) +1)
  }

  for (var i=0; i<bioSize(); i++) {
    wordArray[i] = fake.hacker.noun();
  };
  rawBio = wordArray.toString();
  userBio = rawBio.replace(/,/g, " ");
  return userBio;
}

console.log(randomBio());
