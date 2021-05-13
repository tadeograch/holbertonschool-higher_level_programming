$(function () {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.get(url, function (data, textStatus) {
    const res = data.results;
    for (const i in res) {
      const item = $('<li></li>').text(res[i].title);
      $('#list_movies').append(item);
    }
  });
});
