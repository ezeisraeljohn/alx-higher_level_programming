#!/usr/bin/node

const dict = require('./101-data').dict;

const newObj = {};

for (const userId in dict) {
  if (!newObj[dict[userId]]) {
    newObj[dict[userId]] = [];
  }
  newObj[dict[userId]].push(userId);
}

console.log(newObj);
