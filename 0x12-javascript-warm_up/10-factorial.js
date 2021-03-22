#!/usr/bin/node

const n = parseInt(process.argv[2]);

function factorial (n) {
  if (isNaN(n)) {
    return (1);
  }
  if (n === 0) {
    return (1);
  }
  return (factorial(n - 1) * n);
}

console.log(factorial(n));
