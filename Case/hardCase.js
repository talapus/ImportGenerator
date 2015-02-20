#!/usr/bin/env node

if (!process.argv[2]) {
  console.log("Usage: hardCase [string]");
} else {
  userInput = process.argv[2];
  var getReview = function (userInput) {
    switch (userInput) {
        case 'Toy Story 2':
        console.log("Great story. Mean prospector.");
        break;

        case 'Finding Nemo':
        console.log("Cool animation, and funny turtles.");
        break;

        case 'The Lion King':
        console.log("Great songs.");
        break;

        default:
        console.log("I don't know!");
    }
  };
}
