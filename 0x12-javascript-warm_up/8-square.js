#!/usr/bin/node

const x = Number(process.argv[2]);
let X = '';
let i, j;

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (j = 0; j < x; j++) {
    X += 'X';
  }
  for (i = 0; i < x; i++) {
    console.log(X);
  }
}
