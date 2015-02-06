#!/usr/bin/env node

fs = require('fs');

fs.writeFile('helloworld.txt', 'Hello World!\n', function (err) {
  if (err) return console.log(err);
  console.log('Hello world > helloword.txt');
});
