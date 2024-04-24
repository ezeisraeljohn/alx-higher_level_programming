#!/usr/bin/node

const argvs = require('node:process').argv;
const writeToFile = require('node:fs').writeFile;

/**
 * The writeFile FUnction
 * This function writes to a file
 * @param {file} filename - The file to write to
 * @param {string} data - The string to write to the file
 */
function writeFile (filename, data) {
  writeToFile(filename, data, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
    }
  });
}

writeFile(argvs[2], argvs[3]);
