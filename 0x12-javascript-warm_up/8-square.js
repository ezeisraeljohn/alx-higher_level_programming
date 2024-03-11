#!/usr/bin/node
let i, j;
if (!Number(process.argv[2])) {
  console.log('Missing size');
}

for (i = 0; i < process.argv[2]; i++) {
  for (j = 0; j < process.argv[2]; j++) {
    process.stdout.write('X');
  }
  console.log('');
}
