#!/usr/bin/node

const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let x = 0; x < this.height; x++) {
        for (let y = 0; y < this.width; y++) {
          process.stdout.write(`${c}`);
        }
        console.log();
      }
    }
  }
}
module.exports = Square;
