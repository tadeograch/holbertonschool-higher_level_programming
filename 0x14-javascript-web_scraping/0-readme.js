#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], bar)

function bar (err, data)
  {
  err ? Function("error","throw error")(err) : console.log(data.toString('utf8') );
  };
