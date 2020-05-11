#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const Newlist = list.map(x => x * list.indexOf(x));
console.log(Newlist);
