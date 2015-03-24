#!/usr/bin/env node

var fake = require('faker')

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
