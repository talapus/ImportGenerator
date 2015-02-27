#!/usr/bin/env node

var getReview = function (movie) {
    switch (movie) {
        case 'Toy Story 2':
        return("Great story. Mean prospector.");
        break;

        case 'Finding Nemo':
        return("Cool animation, and funny turtles.");
        break;

        case 'The Lion King':
        return("Great songs.");
        break;

        default:
        return("I don't know!");
    }
};

if (!process.argv[2]) {
  console.log(String.fromCharCode(0x0000,0x2615));
} else {
  userInput = process.argv[2];
  getReview(userInput);
}
