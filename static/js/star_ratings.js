$(document).ready(function() {
    // INDIVIDUAL SERVICE PAGES 
    // Apply the correct width to the orange review stars
    let rating = Number($('#rating').text());
    let percentage = rating * 20;
    $('.fill-ratings').css('width', percentage + "%")


    // Gets the span width of the filled-ratings span
    // this will be the same for each rating
    let starRatingWidth = $('.fill-ratings span').width();
    // Sets the container of the ratings to span width
    // thus the percentages in mobile will never be wrong
    $('.star-ratings').width(starRatingWidth);

    // All REVIEWS PAGE
    $('.review-fill-ratings').each( function () {
        let starId = $(this).prop('id');
        let num = starId.split("-")[2];
        let rating = Number($('#rating-' + num).text());
        let percentage = rating * 20;
        $(this).css('width', percentage + "%");
    });
});