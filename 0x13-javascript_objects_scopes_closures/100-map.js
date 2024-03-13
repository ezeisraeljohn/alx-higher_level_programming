#!/usr/bin/node

const list = require('./100-data').list;

const new_array = list.map((el, index) => {
  return el * index;
});

console.log(new_array);
