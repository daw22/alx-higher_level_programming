#!/usr/bin/node

const { argv } = require('node:process');
const fs = require('fs');

fs.readFile(argv[2], function (err, data) {
  if (err) throw err;
  fs.appendFileSync(argv[4], data);
});

fs.readFile(argv[3], function (err, data) {
  if (err) throw err;
  fs.appendFileSync(argv[4], data);
});
