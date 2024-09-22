$(document).ready(function() {
   let $deleteButtons = $('.btn-delete');

    $deleteButtons.each( function (){
        $(this).on('click', function(e) {
            let serviceId = e.target.getAttribute('data-service_id');
            let reviewId = e.target.getAttribute('data-review_id');
            $('#deleteConfirm').attr('href', `delete/${reviewId}`);
            console.log($('#deleteConfirm').attr('href'));
        });
    });
});
