#!/usr/bin/node

const arr = process.argv.slice(2);
let max1 = 0; let max2 = 0; let i; let j;

for (i = 0; i < arr.length; i++) {
  if (max1 < arr[i]) {
    max1 = arr[i];
  }
}
for (j = 0; j < arr.length; j++) {
  if (max2 < arr[j]) {
    if (arr[j] < max1) {
      max2 = arr[j];
    }
  }
}
if (arr.length === 1) {
  console.log(0);
} else {
  console.log(max2);
}
