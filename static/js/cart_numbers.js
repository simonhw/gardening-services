$('.update-link').click(function(e) {
    let form = $(this).parent().prev('.update-form');
    form.submit();
});

$('.remove-item').click(function(e) {
    var csrfToken = "{{ csrf_token }}";
    console.log(csrfToken);
    let itemId = $(this).attr('id').split('remove_')[1];
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