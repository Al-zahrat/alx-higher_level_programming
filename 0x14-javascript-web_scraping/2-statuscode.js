#!/usr/bin/node
const request = require('request');
const add = process.argv[2];
request(add, function (err, res) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ', res.statusCode);
  }
});
