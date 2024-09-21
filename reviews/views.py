from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import generic
from services.models import Service
from .models import Review
from django.core.paginator import Paginator


class StaffCheck(UserPassesTestMixin, generic.ListView):
    """ Check if user account has staff status """

    def test_func(self):
        return self.request.user.is_staff


def service_reviews(request, service_id):
    """
    View that displays all reviews for a specific service
    """

    service = get_object_or_404(Service, pk=service_id)
    reviews = service.reviews.filter(approved=True)
    review_count = len(reviews)

    paginator = Paginator(reviews, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    unpublished_reviews = service.reviews.filter(approved=False)
    unpublished_review_count = len(unpublished_reviews)
    unpublished_paginator = Paginator(reviews, 6)
    unpublished_page_number = request.GET.get("page")
    unpublished_page_obj = unpublished_paginator.get_page(unpublished_page_number)

    context = {
        'reviews': reviews,
        'review_count': review_count,
        'service': service,
        'page_obj': page_obj,
        'unpublished_reviews': unpublished_reviews,
        'unpublished_review_count': unpublished_review_count,
        'unpublished_page_obj': unpublished_page_obj,
    }

    return render(request, "reviews/reviews.html", context)

class UnpublishedReviews(StaffCheck, generic.ListView):
    """
    View that displays all unpublished reviews for a specific services
    only to user with staff permissions
    """

    def unpublished_reviews(request, service_id):
        
        service = get_object_or_404(Service, pk=service_id)
        reviews = service.reviews.filter(approved=False)
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

        return render(request, "reviews/unpublished_reviews.html", context)


def review_page(request, review_id):
    """
    View that displays an individual service review.
    """

    review = get_object_or_404(Review, pk=review_id)

    context = {
        'review': review,
    }

    return render(request, "reviews/review_page.html", context)
