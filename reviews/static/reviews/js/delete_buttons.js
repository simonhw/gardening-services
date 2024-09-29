$(document).ready(function() {
   let $deleteButtons = $('.btn-delete');

    $deleteButtons.each( function (){
        $(this).on('click', function(e) {
            let reviewId = e.target.getAttribute('data-review_id');
            $('#deleteConfirm').attr('href', `delete/${reviewId}`);
            console.log($('#deleteConfirm').attr('href'));
        });
    });
});
