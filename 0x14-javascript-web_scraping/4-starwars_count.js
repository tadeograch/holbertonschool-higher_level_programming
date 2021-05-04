#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let result = JSON.parse(body).results;
    let num = 0;
    for (let i = 0; i < result.lenght; i++) {
      let character = result[i].characters;
      for (let j = 0; j < character.lenght; j++) {
        if (character[j].includes('18')) {
          num++;
        }
      }
    }
    console.log(num);
  }
});
