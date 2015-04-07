#!/usr/bin/env node

var fake = require('faker');

/*
var showUsage = function() {
  console.log("wordArray: #");
}

var bioSize = function() {
    return (Math.floor(Math.random() * 1500) +1)
}
*/

var userBio = function(input) {
  wordArray = [];

  var bioSize = function() {
    return (Math.floor(Math.random() * 1500) +1)
  }

  for (var i=0; i<bioSize(); i++) {
    wordArray[i] = fake.hacker.noun();
  };
  console.log(wordArray + " ");
}

userBio();
