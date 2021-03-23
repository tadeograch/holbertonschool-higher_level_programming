#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!w || !h) {
      return;
    }
    if (w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let j = 0; j < this.height; j++) {
      for (let i = 0; i < this.width; i++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }
}
module.exports = Rectangle;
