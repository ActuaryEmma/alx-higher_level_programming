#!/usr/bin/node
// defines a square and inherits from Rectangle

class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += 'C';
        }
        console.log(row);
      }
    }
  }
}
module.exports = Square;
