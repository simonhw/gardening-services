from . import views
from django.urls import path

urlpatterns = [
    path(
        '<service_id>/reviews',
        views.service_reviews,
        name='service_reviews'
        ),
    path(
        '<service_id>/unpublished_reviews',
        views.UnpublishedReviews.as_view(),
        name='unpublished_reviews'
        ),
    path(
        '<service_id>/reviews/<review_id>',
        views.review_page,
        name='review_page'
        ),
]