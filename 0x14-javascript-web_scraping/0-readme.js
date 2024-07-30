#!/usr/bin/node
let f = process.argv[2];
let fs = require('fs');
fs.readFile(f, 'utf8', function (err, data = err) {
	console.log(data);
});
