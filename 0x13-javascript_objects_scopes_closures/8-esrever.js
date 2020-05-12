#!/usr/bin/node
/* returns the number of occurrences in a list */
exports.esrever = function (list) {
  const rev = [];
  for (const i in list) {
    rev.unshift(list[i]);
  }
  return (rev);
};
