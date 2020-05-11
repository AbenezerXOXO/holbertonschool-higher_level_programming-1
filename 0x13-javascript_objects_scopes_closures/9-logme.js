#!/usr/bin/node
let a = 0;
exports.logMe = function (item) {
  console.log('%s: %s', a, item);
  a++;
};
