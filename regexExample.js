#!/usr/bin/env node

var string = "one,two,three,four";
var newString = string.replace(/,/g, " ");

console.log("String: ", string);
console.log("newString: ", newString);

