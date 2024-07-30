#!/usr/bin/node
const f = process.argv[2];
const fs = require('fs');
fs.readFile(f, 'utf8', function (err, data = err) {
  console.log(data);
});
