#!/usr/bin/node
// defines a rectangle with constructor w and h

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
