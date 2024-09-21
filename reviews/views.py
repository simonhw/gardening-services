from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import generic
from services.models import Service
from .models import Review
from django.core.paginator import Paginator
from django.contrib import messages


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
    
def publish_review(request, service_id, review_id):
    """
    Method to allow staff users to mark a review as published.
    """
    service = get_object_or_404(Service, pk=service_id)
    review = get_object_or_404(Review, pk=review_id)

    if request.user.is_staff:
        review.approved = True
        review.save()
        messages.success(
            request, f'Review "{ review.title }" successfully published'
        )
    else:
        messages.ERROR(
            request, f'Review "{ review.title }" was not published'
        )
    return redirect('unpublished_reviews', service.id)




def review_page(request, review_id):
    """
    View that displays an individual service review.
    """

    review = get_object_or_404(Review, pk=review_id)

    context = {
        'review': review,
    }

    return render(request, "reviews/review_page.html", context)
