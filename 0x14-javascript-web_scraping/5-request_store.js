#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];
const fs = require('fs');

request(url, (error, response, body) => {
  if (!error) {
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.log(error);
  }
});
