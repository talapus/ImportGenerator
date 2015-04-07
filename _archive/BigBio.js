#!/usr/bin/env node

var fake = require('faker')

var showUsage = function() {
  console.log("BigBio: #");
}


/* old experiments

//var fake = require('faker');

var BigBio = function() {
  var whatever = "test" //fake.company.bsAdjective();

  for (var i=0; i<0; i++) {
    whatever = whatever + " " + fake.company.bsAdjective();
  }
  return(whatever);
  //return('test');
} */

// this returns only one name
//var BigBio = function() {for (var i=0; i<30; i++) {return(fake.name.firstName())}}
// console.log(BigBio());

/* this works, but I don't want to just spew onto the console
var BigBio = function() {for (var i=0; i<30; i++) {console.log(fake.name.firstName())}}
BigBio();
*/

var names = [];
var BigBio = function() {for (var i=0; i<30; i++) {console.log(fake.name.firstName())}}

if (!process.argv[2] || isNaN(+process.argv[2])) {
  showUsage();
} else {
  numWords = +process.argv[2];
  var allWords = fake.lorem.words(numWords);
  for (var i=0; i<allWords.length; i++) {
    console.log(allWords[i]);
  };
}
