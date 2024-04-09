#!/usr/bin/node

function logMe (item) {
  logMe.count = (logMe.count || 0) + 1;
  console.log(logMe.count - 1 + ': ' + item);
}

exports.logMe = logMe;
