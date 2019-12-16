//nav bar
$(document).ready(function(){
    $('.sidenav').sidenav();
  });

  //autocomplete
  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.autocomplete');
    var instances = M.Autocomplete.init(elems, options);
  });
  

  //select options
   $(document).ready(function(){
    $('select').formSelect();
  });

  //review text box
  $('#textarea1').val('New Text');
  M.textareaAutoResize($('#textarea1'));