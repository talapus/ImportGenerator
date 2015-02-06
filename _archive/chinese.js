#!/usr/bin/env node

var fake = require('faker')
fake.locale = "zh_CN"

console.log(fake.name.firstName());
