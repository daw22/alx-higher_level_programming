#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

Object.keys(dict).forEach((key) => { newDict[dict[key]] = []; });
Object.keys(dict).forEach((key) => { newDict[dict[key]].push(key); });

console.log(newDict);
