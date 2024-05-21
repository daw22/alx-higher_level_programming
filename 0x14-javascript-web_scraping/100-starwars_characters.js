#!/usr/bin/node

const request = require('request');
const baseUrl = 'https://swapi-api.alx-tools.com/api/films';
const filmId = process.argv[2];

request(`${baseUrl}/${filmId}`, (err, response, data) => {
  if (!err) {
    const movies = JSON.parse(data);
    movies.characters.forEach((character) => {
      request(character, (error, resp, body) => {
        if (!error) {
          const actor = JSON.parse(body);
          console.log(actor.name);
        } else {
          console.log(error);
        }
      });
    });
  } else {
    console.log(err);
  }
});
