#!/usr/bin/node

const list = require('./100-data').list;

const newArray = list.map((el, index) => {
  return el * index;
});

console.log(list);
console.log(newArray);
