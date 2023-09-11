#!/usr/bin/node
// searches biggest integer in the list of arguments

const num = process.argv.length - 2;
if (isNaN(num < 2)) {
  console.log(0);
} else {
  const list = process.argv.sort();
  console.log(list.reverse()[1]);
}
