#!/usr/bin/env node

var fake = require('faker')

if (!process.argv[2]) {
  console.log("Usage: fakeLoop #");
} else {
  input = +process.argv[2];
  for (var i=0; i < input; i++) {
    console.log((i+1), fake.name.firstName());
  }
}

/*
de
de_AT
de_CH
en
en_AU
en_BORK
en_CA
en_GB
en_IND
en_US
en_au_ocker
es
fa
fr
it
ja
ko
nb_NO
nep
nl
pl
pt_BR
ru
sk
sv
vi
zh_CN
*/
