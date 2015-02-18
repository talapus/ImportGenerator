#!/usr/bin/env node

var getSpecialism = function() {
  specialists = ["Specialist", "Professional", "Executive", "Engineer", "Technician"];
  return (specialists[Math.floor(Math.random() * specialists.length)])
}

for (i=0; i<20; i++) {
  console.log(getSpecialism());
}
