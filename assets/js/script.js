//nav bar
$(document).ready(function(){
    $('.sidenav').sidenav();
  });

  //autocomplete
  $(document).ready(function(){
    $('input.autocomplete').autocomplete({
      data: {
        "Apple": null,
        "Microsoft": null,
        "Google": 'https://placehold.it/250x250'
      },
    });
  });
  

  //select options
   $(document).ready(function(){
    $('select').formSelect();
  });

  //review text box
  $('#textarea1').val('New Text');
  M.textareaAutoResize($('#textarea1'));

  