#!/usr/bin/node

const request = require('request')
const argvs = require('node:process').argv


/**
 * The requestMovieTitle function
 * This function requests a movie title
 * @param {number} id - The Id to be parsed
 */
function requestMovieTitle(id){
  request(`https://swapi-api.alx-tools.com/api/films/${id}`, (error, response, body)=>{
    if (error){
      console.error(error)
    }
    const data = JSON.parse(body)
    console.log(data.title)
  } )
}

requestMovieTitle(argvs[2])