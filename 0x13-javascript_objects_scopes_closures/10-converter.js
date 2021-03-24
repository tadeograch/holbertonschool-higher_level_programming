#!/usr/bin/node

exports.converter = function (base) {
  function number (num) {
    return (num.toString(base));
  }
  return number;
};
