#!/usr/bin/node

const { argv } = require('node:process');

const num = parseInt(argv[2]);
console.log(Number.isNaN(num) ? 'Not a number' : 'My number: ' + num);
