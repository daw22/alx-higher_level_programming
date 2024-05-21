#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

const dict = {};

request(url, (err, response, data) => {
  if (!err) {
    const resp = JSON.parse(data);
    resp.forEach((user) => {
      if (user.completed) {
        dict[user.userId] = dict[user.userId] ? dict[user.userId] + 1 : 1;
      }
    });
    console.log(dict);
  } else {
    console.log(err);
  }
});
