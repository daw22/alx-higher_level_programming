$.get('https://swapi-api.alx-tools.com/api/films/?format=json',
  function (data, textStatus) {
    data.results.forEach((movie) => {
      $('UL#list_movies').append(`<li>${movie.title}</li>`);
    });
  }
);
