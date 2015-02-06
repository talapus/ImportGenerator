#!/usr/bin/env node

var fake = require('faker');
var fs = require('fs');

fake.locale = "ru";

fs.writeFile('chinese.csv', fake.name.firstName(), function (err) {
  if (err) return console.log(err);
  console.log('fake.name.firstName() > chinese.csv');
});
