#!/usr/bin/node
const request = require('request');
const add = process.argv[2];
request(add, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ', res.statusCode);
  }
});
