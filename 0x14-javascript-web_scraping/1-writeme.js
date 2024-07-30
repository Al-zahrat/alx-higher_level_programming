#!/usr/bin/node
const f = process.argv[2];
const s = process.argv[3];
const fs = require('fs');
fs.writeFile(f, s, function (err) {
  if (err) {
    console.log(err);
  }
});
