#!/usr/bin/node
// This script prints a square, the first argument is the size of the square
const myVar = process.argv[2];
if (isNaN(myVar)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myVar; i++) {
    console.log('X'.repeat(myVar));
  }
}
