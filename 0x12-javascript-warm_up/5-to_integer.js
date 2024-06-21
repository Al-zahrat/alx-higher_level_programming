#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length === 0) {
  console.log('Not a number');
} else {
  const x = parseInt(args[0], 10);
  if (isNaN(x)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + x);
  }
}
