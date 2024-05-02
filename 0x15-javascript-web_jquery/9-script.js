#!/usr/bin/node

$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    const name = data.hello;
    $('DIV#hello').text(name);
  });
});
