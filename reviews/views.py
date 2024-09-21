from django.shortcuts import render, get_object_or_404
from services.models import Service
from .models import Review
from django.core.paginator import Paginator


def service_reviews(request, service_id):
    '''
    View that displays all reviews for a specific
    '''

    service = get_object_or_404(Service, pk=service_id)
    reviews = service.reviews.all()
    review_count = len(reviews)

    paginator = Paginator(reviews, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'reviews': reviews,
        'review_count': review_count,
        'service': service,
        'page_obj': page_obj,
    }

    return render(request, "reviews/reviews.html", context)


def review_page(request, review_id):
    '''
    View that displays an individual service review.
    '''

    review = get_object_or_404(Review, pk=review_id)

    context = {
        'review': review,
    }

    return render(request, "reviews/review_page.html", context)
