#!/usr/bin/node
// This script prints a message depending of the number of arguments passed
const myVar = process.argv[2];
if (myVar >= process.argv[2]) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
