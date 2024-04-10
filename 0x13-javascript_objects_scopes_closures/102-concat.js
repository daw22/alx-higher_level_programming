#!/usr/bin/node

const fs = require('fs');

fs.readFile('./fileA', function (err, data) {
  if (err) throw err;
  fs.appendFileSync('./fileC', data);
});

fs.readFile('./fileB', function (err, data) {
  if (err) throw err;
  fs.appendFileSync('./fileC', data);
});
