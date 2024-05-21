#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];
const fs = require('fs');

request(url, function (error, response, body) {
  if (!error && body) {
    fs.writeFileSync(filePath, body, { encoding: 'utf8' });
  } else {
    console.log(error);
  }
});
