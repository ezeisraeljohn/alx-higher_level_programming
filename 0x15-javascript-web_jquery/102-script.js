#!/usr/bin/node

$(document).ready(function () {
  const code = $('INPUT#language_code').val();
  $.get(`https://hellosalut.stefanbohacek.dev/?lang=${code}`, function (data) {
    $('INPUT#btn_translate').click(function () {
      $('DIV#hello').text(`${data['hello']}`);
    });
  });
});
