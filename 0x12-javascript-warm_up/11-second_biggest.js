#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length < 3) {
  console.log(0);
} else {
  let biggest = argv[2];
  for (let i = 2; i < argv.length + 2; i++) {
    if (argv[i] > biggest) {
      biggest = argv[i];
    }
  }
  let diff = biggest;
  for (let i = 2; i < argv.length + 2; i++) {
    if (argv[i] !== biggest && biggest - argv[i] < diff) {
      diff = biggest - argv[i];
    }
  }
  console.log(biggest - diff);
}
