$(document).ready(function(){
    $("a").on('click', function(event){
        if (this.Link !== ""){
            event.preventDefault();
            var Link = this.Link;
            $('html, body').animate({
                scrollTop: $(Link).offset().top
            }, 2000, function(){
                window.location.Link = Link;
            });
        }
    });
});

function openForm(){
    document.getElementById("myForm").style.display = "block";
}

function closeForm(){
    document.getElementById("myForm").style.display = "none";
    this.Close();
}

(function ($) {
    'use strict';

    var form = $('.form-container'),
        message = $('.success_message'),
        form_data;

    //success function
    function done_func(response) {
        message.fadeIn()
        message.html(response);
        setTimeout(function () {
            message.fadeOut();
        }, 5000);

        form.find('input:not([type="submit"]), textarea').val('');
    }

    //fail function
    function fail_func(data) {
        message.fadeIn()
        message.html(data.responseText);
        setTimeout(function () {
            message.fadeOut(5000);
        }, 5000);
    }

    form.submit(function (e) {
        e.preventDefault();
        form_data = $(this).serialize();
        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: form_data
        })
        .done(done_func)
        .fail(fail_func);
    });
})(jQuery);
