from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import View
from django.utils.html import strip_tags

from .models import Review
from .forms import ReviewForm
from accounts.models import UserAccount
from services.models import Service
from django.core.paginator import Paginator

from django.contrib import messages
from django.http import HttpResponseBadRequest
from django.core.exceptions import PermissionDenied


class StaffCheck(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff


class ServiceReviews(View):
    """
    View that shows reviews for a particular service ordered by date of
    creation.
    """

    def get(self, request, service_id):
        """
        Function to handle pagination of reviews
        """

        service = get_object_or_404(Service, pk=service_id)
        reviews = service.reviews.filter(approved=True).order_by('created_on')
        review_count = len(reviews)

        paginator = Paginator(reviews, 6)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        if request.user.is_authenticated:
            ordered = self.service_history(request, service)
        else:
            ordered = False

        context = {
            'reviews': reviews,
            'review_count': review_count,
            'service': service,
            'page_obj': page_obj,
            'ordered': ordered,
        }

        return render(request, "reviews/reviews.html", context)

    def service_history(self, request, current_service):
        """
        Function to check if a user has previously ordered a particular
        service.
        """

        ordered = False
        account = get_object_or_404(UserAccount, user=request.user)
        orders = account.orders.all()
        for order in orders:
            for item in order.lineitems.all():
                if item.service.id == current_service.id:
                    ordered = True
                    break
        return ordered


class UnpublishedReviews(StaffCheck, View):
    """
    View that shows unpublished reviews for a particular service
    ordered by date of creation.
    """

    def get(self, request, service_id):

        service = get_object_or_404(Service, pk=service_id)
        reviews = service.reviews.filter(approved=False).order_by('created_on')
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


@login_required
def create_review(request, service_id):
    """
    Method to handle the review form.

    Processes and validates the user-submitted data. Saves data and
    assigns user as the review owner.
    Messages are displayed on successful review creation.
    If validation fails, the form is re-rendered with appropriate error
    messages.
    """

    service = get_object_or_404(Service, pk=service_id)

    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.reviewer = request.user
            review.service = service
            review.save()
            messages.success(
                request, "Review submitted pending approval."
            )
            return redirect('service_reviews', service.id)
        else:
            review_form = ReviewForm(data=request.POST)
            return render(
                request, 'reviews/create_review.html',
                {
                    'review_form': review_form,
                }
            )

    review_form = ReviewForm()

    return render(
        request, 'reviews/create_review.html',
        {
            'review_form': review_form,
            'service': service,
        }
    )


@user_passes_test(lambda u: u.is_staff)
def publish_review(request, service_id, review_id):
    """
    Method to allow staff users to toggle the publication state of a
    review.
    """
    service = get_object_or_404(Service, pk=service_id)
    review = get_object_or_404(Review, pk=review_id)

    if request.user.is_staff:
        try:
            if review.approved:
                review.approved = False
                review.save()
                messages.success(
                    request,
                    f'Review "{review.title}" successfully unpublished'
                )
                return redirect('service_reviews', service.id)
            else:
                review.approved = True
                review.save()
                messages.success(
                    request,
                    f'Review "{review.title}" successfully published'
                )
                return redirect('unpublished_reviews', service.id)

        except Exception as e:
            messages.error(
                request,
                f"There was a problem changing that review's status: {e}"
            )
        return redirect('service_reviews', service.id)


@login_required
def edit_review(request, service_id, review_id):
    """
    Allow users to edit their own reviews. Take the review id and
    pre-fill the form with the correct data for the user to edit.
    """

    service = get_object_or_404(Service, pk=service_id)
    review = get_object_or_404(Review, pk=review_id)

    if review.reviewer == request.user:
        if request.method == 'GET':
            review.content = strip_tags(review.content)
            review_form = ReviewForm(instance=review)
            return render(
                request,
                'reviews/create_review.html',
                {
                    'review_form': review_form,
                    'service': service,
                    'service_id': service_id,
                    'review_id': review_id,
                    'edit_review': True
                }
            )
        elif request.method == 'POST':
            review_form = ReviewForm(request.POST, instance=review)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                # Mark the review as unpublished if the user editing it is
                # not a staff user.
                if not request.user.is_staff:
                    review.approved = False
                review.save()
                messages.success(
                    request,
                    f'Review "{review.title}" successfully edited pending\
                    approval.'
                    )
                if not request.user.is_staff:
                    return redirect('service_reviews', service_id)
                elif request.user.is_staff and review.approved:
                    return redirect('service_reviews', service_id)
                else:
                    return redirect('unpublished_reviews', service_id)
            else:
                review_form = ReviewForm(data=request.POST)
                return render(
                    request,
                    'reviews/create_review.html',
                    {
                        'review_form': review_form,
                        'service': service,
                        'service_id': service_id,
                        'review_id': review_id,
                        'edit_review': True
                    }
                )
                messages.error(request, 'Please fully complete the form')
        else:
            return HttpResponseBadRequest('Unsupported request method.')
    else:
        raise PermissionDenied


@login_required
def delete_review(request, service_id, review_id):
    """
    Method to allow staff users and review owners to delete a review
    """
    service = get_object_or_404(Service, pk=service_id)
    review = get_object_or_404(Review, pk=review_id)

    page_check = review.approved

    if request.user.is_staff or request.user == review.reviewer:
        review.delete()
        messages.success(
            request, f'Review "{review.title}" successfully deleted'
        )
    else:
        messages.ERROR(
            request, f'Review "{review.title}" could not be deleted. Please\
                try again later.'
        )
    # Return user to the correct review page
    if page_check:
        return redirect('service_reviews', service.id)
    elif not page_check:
        return redirect('unpublished_reviews', service.id)
    else:
        return redirect('home')
