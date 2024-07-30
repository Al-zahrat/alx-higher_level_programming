#!/usr/bin/node
let request = require('request');
let add = process.argv[2];
request(add, function (err, res, body) {
	if (err) {
		console.log(err);
	} else {
		console.log('code: ', res['statusCode']);
	}
});
