#!/usr/bin/node

const { argv } = require('node:process');

function add (a, b) {
  if (Number.isNaN(a) || Number.isNaN(b)) {
    return (NaN);
  }
  return (a + b);
}
console.log(add(parseInt(argv[2]), parseInt(argv[3])));
