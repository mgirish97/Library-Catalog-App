// JQuery to hide and show Sample Book results card when clicking search buttun and clicking home button

$(document).ready(function () {

    $('.search-button').click(function () { 
        $('.sample-book').show();
    })

    $('.home-btn').click(function () {  
        $('.sample-book').hide();
    })

})