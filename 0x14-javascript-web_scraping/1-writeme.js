#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const data = process.argv[3] + "\n";

fs.writeFile(filePath, data,
  {
    encoding: 'utf8',
    flag: 'w'
  },
  (err) => {
    if (err) {
      console.log(err);
    }
  }
);
