#!/usr/bin/env node

var fake = require('faker');
var fs = require('fs');

var locales = ['de', 'de_AT', 'de_CH', 'en', 'en_AU','en_BORK','en_CA','en_GB','en_IND','en_US','en_au_ocker','es','fa','fr','it','ja','ko','nb_NO','nep','nl','pl','pt_BR','ru','sk','sv','vi','zh_CN']



/*
console.log("Number of items in someList: " + locales.length);

for (i=0; i < locales.length; i++) {
  fake.locale = locales[i];
  console.log((i+1), locales[i], fake.name.firstName());
} */





if (!process.argv[2] || isNaN(+process.argv[2])) {
  console.log("Usage: csvGen #");

} else { // only write a file if the user indicates how many records
  userInput = +process.argv[2];

  for (var z=0; z<locales.length; z++) { // write one file per locale in 'locales'
    var stream = fs.createWriteStream("en_US.csv");

    stream.once('open', function(fd) { // open fs stream

      for (i=0; i<userInput; i++) { // write the number of records indicated by the user
        stream.write(fake.name.firstName() + "\n");
      }
      stream.end();
    }
    console.log(localeKey + ".csv created");
  });

}
