#!/usr/bin/env node

var fake = require('faker')

locales = ['de',
  'de_AT',
  'de_CH',
  'en',
  'en_AU',
  'en_BORK',
  'en_CA',
  'en_GB',
  'en_IND',
  'en_US',
  'en_au_ocker',
  'es',
  'fa',
  'fr',
  'it',
  'ja',
  'ko',
  'nb_NO',
  'nep',
  'nl',
  'pl',
  'pt_BR',
  'ru',
  'sk',
  'sv',
  'vi',
  'zh_CN']

console.log("Number of items in someList: " + locales.length);

for (i=0; i < locales.length; i++) {
  fake.locale = locales[i];
  console.log((i+1), locales[i], fake.name.firstName());
}
