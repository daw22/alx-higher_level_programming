#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

let count = 0;

request(url, function (error, response, body) {
  if (!error && response.body) {
    const data = JSON.parse(body);
    data.results.forEach((movie) => {
      movie.characters.forEach((character) => {
        if (character.includes('18')) {
          count++;
        }
      });
    });
    console.log(count);
  } else {
    console.log(error);
  }
});
