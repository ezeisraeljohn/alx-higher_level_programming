#!/usr/bin/node

function factorial(a) {
  if (a === 1) {
    return 1;
  }
  return a * factorial(a - 1);
}

console.log(parseInt(process.argv[2]));
