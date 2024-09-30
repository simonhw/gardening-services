/*jshint jquery: true */
$(document).ready(function() {
    // For pre-filled data, check if continue button should be enabled
    continueCheck();

    // If the user has not entered data into all required input fields, do not
    // allow the user to move to the Payment Details section of the form.
    $('.details-fields input[required]').bind('keyup',function() {
        continueCheck();
    });

    function continueCheck() {
        if( allFilled() ) {
            $('#show-payment').removeAttr('disabled');
        } else {
            $('#show-payment').prop("disabled", true);
        }
    }

    function allFilled() {
        var filled = true;
        $('.details-fields input[required]').each(function() {
            console.log('this is', $(this).val());
            if ($(this).val() == ''){
                filled = false;
            }
        });
        return filled;
    }

    // Navigate back to the Address Details section
    $('.show-address, .adjust-address').click(function() {
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

    // Show the Payment Details section
    $('.show-payment, .adjust-payment').click(function() {

        // If email field is valid, allow user to move to the payment details
        // otherwise inform the user of their error.
        if ( $('#id_email')[0].checkValidity() ) {
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
        } else {
            $('#id_email')[0].reportValidity();
        }
    });

    // Show the Order Review section
    $('.show-review').click(function() {
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

        // Show the address data in the Order Review section
        $('#review_street_address1').text($('#id_street_address1').val());
        $('#review_street_address2').text($('#id_street_address2').val());
        $('#review_town_or_city').text($('#id_town_or_city').val());
        $('#review_county').text($('#id_county').val());
        $('#review_eircode').text($('#id_eircode').val());
    });
});