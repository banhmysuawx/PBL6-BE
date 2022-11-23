from django.urls import path

from reviews.views import ReviewListView,ReviewDetailView,ReviewCreateListView

urlpatterns = [
    path('reviews', ReviewListView.as_view()),
    path('reviews/create', ReviewCreateListView.as_view()),
    path('reviews/<int:pk>', ReviewDetailView.as_view()),
]