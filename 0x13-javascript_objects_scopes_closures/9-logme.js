#!/usr/bin/node

let staticVariable = 0;

exports.logMe = function (item) {
  console.log(`${staticVariable}: ${item}`);
  staticVariable++;
};
