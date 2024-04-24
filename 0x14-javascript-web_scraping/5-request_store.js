#!/usr/bin/node

const request = require('request');
const argvs = require('node:process').argv;
const fs = require('node:fs');

/**
 * storeWebContent function:
 * This function stores the value of a web content into a file
 * @param {Url} url
 * @param {file} filepath
 */
function storeWebContent (url, filepath) {
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    }
    // Write the body content to the file
    fs.writeFile(filepath, body, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  });
}
storeWebContent(argvs[2], argvs[3]);
