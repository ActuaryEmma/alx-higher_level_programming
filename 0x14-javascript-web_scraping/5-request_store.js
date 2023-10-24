#!/usr/bin/node
// scripts that reads and prints the content of a file
// fs.readfile(filename, encoding, callback_function)
// filename - name of the file to read or the path of the file
// encoding - defaults value is utf8
// callback_function - called after reading the file.
// callback functions contains err(error occured) and data(content of the file)
const process = require('process');
const fs = require('fs');
const path = require('path');
const request = require('request');

if (process.argv.length !== 4) {
  const script = path.basename(process.argv[1]);
  console.log(`Usage: node ${script} <url> <filepath>`);
  process.exit(1);
}
const url = process.argv[2];
const filepath = process.argv[3];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  fs.writeFile(filepath, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
