#!/usr/bin/node

const { argv } = require('node:process');

console.log(argv[2] ? argv[2] : 'No argument');
