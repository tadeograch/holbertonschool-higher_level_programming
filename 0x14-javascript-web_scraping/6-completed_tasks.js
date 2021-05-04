#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    const dict = {};
    let i = 0;
    while (i in tasks) {
      const uId = tasks[i].userId;
      if (tasks[i].completed) {
        if (uId in dict) {
          dict[uId] += 1;
        } else {
          dict[uId] = 1;
        }
      }
      i++;
    }
    console.log(dict);
  }
});
