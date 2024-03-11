#!/usr/bin/node
if (process.argv.length >= 4) {
  console.log('Arguements found');
} else if (process.argv.length === 3) {
  console.log('Arguement found');
} else {
  console.log('No argument');
}
