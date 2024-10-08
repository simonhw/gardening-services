from . import views
from django.urls import path

urlpatterns = [
    path(
        '<service_id>/reviews/',
        views.ServiceReviews.as_view(),
        name='service_reviews'
        ),
    path(
        '<service_id>/unpublished_reviews/',
        views.UnpublishedReviews.as_view(),
        name='unpublished_reviews'
        ),
    path(
        '<service_id>/leave_review/',
        views.create_review,
        name='create_review'
    ),
    path(
        '<service_id>/reviews/<review_id>/',
        views.review_page,
        name='review_page'
        ),
    path(
        '<service_id>/reviews/publish/<review_id>/',
        views.publish_review,
        name='publish_review'
        ),
    path(
        '<service_id>/reviews/edit/<review_id>/',
        views.edit_review,
        name='edit_review'
        ),
    path(
        '<service_id>/unpublished_reviews/delete/<review_id>/',
        views.delete_review,
        name='delete_review'
        ),
]
