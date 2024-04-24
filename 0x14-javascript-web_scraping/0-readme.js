#!/usr/bin/node

const argvs = require('node:process').argv;
const fs = require('node:fs');

/**
 * Read data from a file
 * This function reads data from a file and outputs the data
 * @param {file} filename - The file to read the data from
 */
function readFile (filename) {
  fs.readFile(filename, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
    }
    console.log(data);
  });
}

readFile(argvs[2]);
