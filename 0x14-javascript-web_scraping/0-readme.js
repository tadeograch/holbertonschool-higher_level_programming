#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], bar);

function bar (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString('utf8'));
  }
}
