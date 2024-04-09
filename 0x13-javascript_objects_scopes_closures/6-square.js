#!/usr/bin/node

const SquareParent = require('./5-square');

class Square extends SquareParent {
  charPrint (character = 'X') {
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += character;
      }
      console.log(line);
    }
  }
}

module.exports = Square;
