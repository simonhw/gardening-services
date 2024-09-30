/*jshint jquery:true */
$(document).ready(function() {
    $('.update-link').click(function() {
        let form = $(this).parent().prev('.update-form');
        form.submit();
    });

    $('.remove-item').click(function() {
        var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        let itemId = $(this).data('item-id');
        let size = $(this).data('size');
        let surface = $(this).data('surface');
        let cuts = $(this).data('cuts');
        let url = `/cart/remove/${itemId}/`;
        var data = {'csrfmiddlewaretoken': csrfToken, 'size': size, 'surface': surface, 'cuts': cuts};

        $.post(url, data)
        .done(function() {
            location.reload();
        });
    });
});