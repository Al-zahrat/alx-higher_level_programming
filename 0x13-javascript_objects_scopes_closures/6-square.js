#!/usr/bin/node
const SquareX = require('./5-square.js');
class Square extends SquareX {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
