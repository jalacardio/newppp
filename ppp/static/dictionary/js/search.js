function fillDataList(data_list_id, optionList) {
    var dl = document.getElementById(data_list_id),
    len = optionList.length;
    dl.innerHTML = '';
    for (var i = 0; i < len; i += 1) {
        var option = document.createElement('div');
        var word = optionList[i]['word'];
        data = "<a href='/dictionary/translation/" + word + "'/>" + word + "</a>"
        option.innerHTML = data;
        dl.appendChild(option);
    }
}

var delay = (function(){
  var timer = 0;
  return function(callback, ms){
  clearTimeout (timer);
  timer = setTimeout(callback, ms);
 };
})();

$('#vocab-search').keyup(function() {
  delay(function(){
   var keyword = document.getElementById("vocab-search").value;
    $.get("http://0.0.0.0:8090/dictionary/search/?word=" + keyword, function(data, status){
        fillDataList("search-vocab-result", data['result']);
      });
  }, 1000 );
});