#!/usr/bin/node

const request = require('request')
const argvs = require('node:process').argv


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