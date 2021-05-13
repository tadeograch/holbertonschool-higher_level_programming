$(function () {
  $('#add_item').click(function () {
    const item = $('<li></li>').text('Item');
    $('ul.my_list').append(item);
  });
});
