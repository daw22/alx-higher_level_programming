$('document').ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?';
  $('INPUT#btn_translate').on('click', function () {
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
