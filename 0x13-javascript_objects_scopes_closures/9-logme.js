#!/usr/bin/node
/* returns the number of occurrences in a list */
let args = 0;
exports.logMe = function (item) {
  console.log(`${args}: ${item}`);
  args++;
};
