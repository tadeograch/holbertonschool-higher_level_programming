#!/usr/bin/node

const n = Number(process.argv[2]);
if (isNaN(n)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + n);
}
