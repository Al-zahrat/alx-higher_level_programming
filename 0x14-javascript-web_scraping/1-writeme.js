#!/usr/bin/node
let f = process.argv[2];
let s = process.argv[3];
let fs = require('fs');
fs.writeFile(f, s, function (err) {
	if (err) {
		console.log(err);
	}
});
