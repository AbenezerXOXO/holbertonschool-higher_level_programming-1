#!/usr/bin/node
exports.esrever = function (list) {
  let rev = '';
  let i;
  for (i = list.length - 1; i >= 0; i++) {
    rev += list[i];
  }
  return rev;
}
