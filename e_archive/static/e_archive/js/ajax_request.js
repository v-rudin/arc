
function set_paginator(msg){
   // alert('set page_num '+msg);
    document.getElementById("page_num").value = msg;
    //var msg1 = $('#filter_form').serialize();
    Get_Filter();

}

function Get_Filter() {
    var msg   = $('#filter_form').serialize();
    ShowList(msg);
}


function ShowList(msg) {

      //  alert(msg);
        //alert('dwe');
		$.ajax({
          type: 'POST',
          url: location.href,
          data: msg,
          success: function(data) {
            $('#table_div').html(data);
          },
          error:  function(xhr, str){
	    alert('Возникла ошибка: ' );
          }
        });
}



