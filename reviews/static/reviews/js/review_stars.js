$(document).ready(function() {
    let $radios = $('.form-check-input');  // Select all radio inputs
    let $stars = $('.form-check-label'); // Select all star labels

    // Function to apply or remove the orange colour of a star
    function updateStars(index) {
        $stars.each(function(i) {
            if (i <= index) {
                $(this).addClass('form-star-selected');
            } else {
                $(this).removeClass('form-star-selected');
            }
        });
    }

    // Add orange color on hover
    $stars.hover(
        function() {
            let index = $stars.index($(this));
            updateStars(index);
        },
        function() {
            let selected = $('.form-check-input:checked');
            if (selected.length) {
                let selectedIndex = $radios.index(selected);
                updateStars(selectedIndex);
                $('.form-check-label').removeClass('invalid');
                $('#rating-validation').addClass('d-none')
            } else {
                updateStars(-1);
            }
        }
    );

    // Custom Form Validation
    $('#reviewForm').on('submit', function(e) {
        let title = $.trim($('input[name="title"]').val());
        let content = $.trim($('textarea[name="content"]').val());
        let rating = $('input[name="rating"]:checked').length > 0;
        console.log('content', content);
        
        if (!title){
            e.preventDefault();
            console.log('!title')
            $('#id_title').addClass('input-border-red');
            $('#id_content').removeClass('input-border-red');
            $('.form-check-label').removeClass('invalid');
            $('#title-validation').removeClass('d-none').text('Title cannot be empty!');
        } else if (!content) {
            e.preventDefault();
            console.log('!content')
            $('#id_title').removeClass('input-border-red');
            $('#id_content').addClass('input-border-red');
            $('.form-check-label').removeClass('invalid');
            $('#content-validation').removeClass('d-none').text('You must write a review!');

        } else if (!rating) {
            e.preventDefault();
            console.log('!rating')
            $('#id_title').removeClass('input-border-red');
            $('#id_content').removeClass('input-border-red');
            $('.form-check-label').addClass('invalid');
            $('#rating-validation').removeClass('d-none').text('You must provide a rating!');
        } else {
            $('#validation-message').addClass('d-none')
            $('#reviewForm').submit();
        }
    });

    // Remove red border from fields when user enters text.
    $('input[name="title"]').on('keyup', function(){
        $('#id_title').removeClass('input-border-red');
        $('#title-validation').addClass('d-none')
    });
    $('textarea[name="content"]').on('keyup', function(){
        $('#id_title').removeClass('input-border-red');
        $('#content-validation').addClass('d-none')
    });
});