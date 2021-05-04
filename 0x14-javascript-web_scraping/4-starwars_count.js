#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const character = 'https://swapi-api.hbtn.io/api/people/18/';
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    let num = 0;
    for (let i = 0; i < results.lenght; i++) {
      for (let j = 0; i < results[i].characters; j++) {
        if (results[i].characters[j] === character) {
          num++;
        }
      }
    }
    console.log(num);
  }
});
