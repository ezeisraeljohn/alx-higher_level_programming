#!/usr/bin/node

$(document).ready(function () {
  const lang_code = $('INPUT#language_code').val();
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + lang_code;
  $.get(url, function (data) {
    $('INPUT#btn_translate').click(function () {
      $('DIV#hello').text(`${data.hello}`);
    });
    $('INPUT#btn_translate').keypress(function (event) {
      if (event.which == 13) {
        $('DIV#hello').text(`${data.hello}`);
      }
    });
  });
});
