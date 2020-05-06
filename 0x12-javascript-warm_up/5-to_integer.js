#!/usr/bin/node
// This script print a message if the first argument can be converted to an int
const myVar = process.argv[2];
if (isNaN(myVar)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(myVar)}`);
}
