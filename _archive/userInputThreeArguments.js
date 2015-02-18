#!/usr/bin/env node

var fake = require('faker');

if (!process.argv[2] || !process.argv[3]) {
  console.log("Ghur?");
} else {
  console.log(fake.hacker.phrase());
}
