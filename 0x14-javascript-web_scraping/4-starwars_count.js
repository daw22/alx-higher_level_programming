#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

let count = 0;

request(url, function (error, response, body) {
  if (!error && response.body) {
    const movies = JSON.parse(body).results;
    for (const movie in movies) {
      const m = movies[movie];
      for (const character in m.characters) {
        const c = m.characters[character];
        if (c.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log(error);
  }
});
