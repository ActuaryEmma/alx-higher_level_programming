#!/usr/bin/node
// computes and print a factorial

function factorial (n) {
  if (isNaN(n) || (n === 1)) {
    return 1;
  } else {
    return (n * factorial(n - 1));
  }
}
const firstNum = parseInt(process.argv[2]);
console.log(factorial(firstNum));
