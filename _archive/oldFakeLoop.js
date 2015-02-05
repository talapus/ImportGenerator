#!/usr/bin/env node

// requirements

var fake = require('faker');

// variables


// functions
var getInput = function () {
  if (!process.argv[2]) {
    loops = 1;
  } else {
    loops = process.argv[2];
  }
}

var displayOutput = function () {
  for (i = 0; i < loops; i++) {
    console.log(i+1, fake.company.bsBuzz());
  }
}

// main

getInput();
displayOutput();

