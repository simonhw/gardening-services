/*jshint jquery: true */
$(document).ready(function() {
   let $deleteButtons = $('.btn-delete');

    // Add event listener to each button and get the ID to delete the correct review
    $deleteButtons.each( function (){
        $(this).on('click', function(e) {
            let reviewId = e.target.getAttribute('data-review_id');
            $('#deleteConfirm').attr('href', `delete/${reviewId}`);
        });
    });
});
