#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const res = JSON.parse(body).results;
    let num = 0;
    for (const i in res) {
      const chars = res[i].characters;
      for (const j in chars) {
        if (chars[j].includes('18')) {
          num++;
        }
      }
    }
    console.log(num);
  }
});
