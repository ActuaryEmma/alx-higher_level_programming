#!/usr/bin/node
// prints a square

const sqSize = parseInt(process.argv[2]);
let string = '';
if (isNaN(sqSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sqSize; i++) {
    for (let j = 0; j < sqSize; j++) {
      string += 'x';
    }
    if (i < sqSize - 1) {
      string += '\n';
    }
  }
  console.log(string);
}
