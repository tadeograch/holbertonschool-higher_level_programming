#!/usr/bin/node

exports.esrever = function (list) {
  let min = 0;
  let max = list.length - 1;
  while (max > min) {
    const temp = list[max];
    list[max] = list[min];
    list[min] = temp;
    max--;
    min++;
  }
  return (list);
};
