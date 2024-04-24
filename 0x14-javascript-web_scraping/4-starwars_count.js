#!/usr/bin/node

const request = require('request');

/**
 * characterAppearanceCount function
 * This function counts the number of times a character appear in films
 */
function characterAppearanceCount () {
  request('https://swapi-api.alx-tools.com/api/films/', (error, response, body) => {
    if (error) {
      console.error(error);
    }
    const data = JSON.parse(body);
    const antilles = 'https://swapi-api.alx-tools.com/api/people/18/';
    let count = 0;
    for (let i = 0; i < data.results.length; i++) {
      if (data.results[i].characters.includes(antilles)) {
        count++;
      }
    }
    console.log(count);
  });
}

characterAppearanceCount();
