//
// $("#contact_form_id").on('click', function () {
//     $('#contact_form_alert').show();
// });

$("#submitForm").on('click', function () {
    $.ajax({
        // url: '{%url "contact_form" %}',
        url: '/contact/',
        type: "POST",
        data: $('#contact_form').serialize(),
        success: function (data) {
            if (data['result'] == 'success') {
                $('#contact_form_id').modal('hide')
                show_alert(data['message']);
                console.log('ok');
                $('#contact_form input').val('');
            } else if (data['result'] == 'error') {
                console.log('error');
            }
        },
        error : function(xhr,errmsg,err) {
            console.log('error dont send');
            // console.log(err);
            // $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
            //     " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            // console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
});



function show_alert(message) {
    $('#contact_form_alert').html('<div class="alert alert-success">' +
                            '<button type="button" class="close" data-dismiss="alert">&times;</button>' + message +
                            '<div>');
    $(".alert").delay(3000).fadeOut(
      "normal",
      function(){
        $(this).remove();
      });
    // setTimeout(function () {
    //     $("#contact_form_alert").alert('close');
    // }, 6000);
}

