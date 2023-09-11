#!/usr/bin/node
// Script that prints My number: <first argument converted in integer>
// parseInt - pass a string and extract int value

const num = parseInt(process.argv[2]);
// isNaN - not a number
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
