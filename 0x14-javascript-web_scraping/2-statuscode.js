#!/usr/bin/node

const argvs = require('node:process').argv;
const request = require('request');

/**
 * requestStatus function
 * The function to request a status
 * @param {url} url - The url to get the response from
 */
async function requestStatus (url) {
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    }
    console.log('code:', response.statusCode);
  });
}

requestStatus(argvs[2]);
