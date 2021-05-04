#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    let uId = 1;
    let dict = {};
    let i = 0;
    while (i in tasks) {
      let done = 0;
      while (tasks[i].userId === uId) {
        if (tasks[i].completed) {
          done++;
        }
        i++;
      }
      if (done > 0) {
        dict[uId.toString()] = done;
      }
      uId++;
    }
    console.log(dict);
  }
});
