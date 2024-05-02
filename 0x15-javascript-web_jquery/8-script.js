#!/usr/bin/node

$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    films = data.results;
    titles = [];
    films.forEach(film => {
      titles.push(film.title);
    });

    titles.forEach(title => {
      $('ul#list_movies').append(`<li> ${title} </li>`);
    });
  });
});
