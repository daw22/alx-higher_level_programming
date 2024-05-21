#!/usr/bin/node

const request = require('request');
const baseUrl = 'https://swapi-api.alx-tools.com/api/films';
const filmId = process.argv[2];

let count = 0;
function printActors (actors) {
  if (count >= actors.length) {
    return;
  }
  request(actors[count], (err, res, body) => {
    if (!err) {
      const actor = JSON.parse(body).name;
      console.log(actor);
      count++;
      printActors(actors, count);
    } else {
      console.log(err);
    }
  });
}

request(`${baseUrl}/${filmId}`, (err, response, data) => {
  if (!err) {
    const movies = JSON.parse(data);
    printActors(movies.characters);
  } else {
    console.log(err);
  }
});
