// Code adapted from Boutique Ado walkthrough
$(document).ready(function() {
    let reasonSelected = $('#id_contact_reason').val();
    if ( !reasonSelected ) {
        $('#id_contact_reason').css('color', '#595c5f');
    }
    $('#id_contact_reason').change(function() {
        let reasonSelected = $('#id_contact_reason').val();
        if ( !reasonSelected ) {
            $(this).css('color', '#595c5f');
        } else {
            $(this).css('color', '#000');
        }
    });
});
