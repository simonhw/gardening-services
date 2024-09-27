$(document).ready(function() {
    let cartOffcanvas = $('#offcanvasRight');
    let serviceAdded = $('#serviceAdded').text();
    let successToast = $('.toast-success');

    if ( serviceAdded && window.innerWidth >= 992) {
        new bootstrap.Offcanvas(cartOffcanvas).show();
        successToast.addClass('d-none');
    }
});
