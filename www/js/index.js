var input = document.getElementById("countries");
var awesomplete = new Awesomplete(input, {
  minChars: 1,
  autoFirst: true
});

$("input").on("keyup", function(){
  $.ajax({
    url: 'http://104.196.185.23:8080/?search=' + this.value,
    type: 'GET',
    dataType: 'json'
  })
  .success(function(data) {
    var list = [];
    $.each(data, function(key, value) {
      list.push(value.name);
    });
    awesomplete.list = list;
  });
});
