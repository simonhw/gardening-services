$('.details-fields input[required]').bind('keyup',function() {

    if( allFilled() ) {
        $('#show-payment').removeAttr('disabled');
    } else {
        $('#show-payment').prop("disabled", true);
    }

    function allFilled() {
        var filled = true;
        $('.details-fields input[required]').each(function() {
            if($(this).val() == '') filled = false;
        });
        return filled;
    }
});

$('.show-address, .adjust-address').click(function(e) {
    $('.details-fields').removeClass('d-none');
    $('.payment-fields').addClass('d-none');
    $('.review-order').addClass('d-none');

    $('#step-1').addClass('active');
    $('#step-2').removeClass('active');
    $('#step-2').children().removeClass('dark');
    $('.line-1').removeClass('dark');
    $('.line-2').removeClass('dark');
    $('#step-3').removeClass('active');
    $('#step-3').children().removeClass('dark');
});

$('.show-payment, .adjust-payment').click(function(e) {

    $('.details-fields').addClass('d-none');
    $('.payment-fields').removeClass('d-none');
    $('.review-order').addClass('d-none');

    $('#step-1').removeClass('active');
    $('#step-2').addClass('active');
    $('#step-2').children().addClass('dark');
    $('.line-1').addClass('dark');
    $('.line-2').removeClass('dark');
    $('#step-3').removeClass('active');
    $('#step-3').children().removeClass('dark');
});

$('.show-review').click(function(e) {
    $('.details-fields').addClass('d-none');
    $('.payment-fields').addClass('d-none');
    $('.review-order').removeClass('d-none');

    $('#step-1').removeClass('active');
    $('#step-2').removeClass('active');
    $('#step-2').children().addClass('dark');
    $('.line-1').addClass('dark');
    $('.line-2').addClass('dark');
    $('#step-3').addClass('active');
    $('#step-3').children().addClass('dark');
});