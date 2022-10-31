from django.urls import path

from reviews.views import ReviewsListAPI,ReviewsDetailAPI,ReviewsCreateAPI,ReviewsUpdateAPI,ReviewsDeleteAPI

urlpatterns = [
    path('reviews', ReviewsListAPI.as_view()),
    path('reviews/create', ReviewsCreateAPI.as_view()),
    path('reviews/<int:id>', ReviewsDetailAPI.as_view()),
    path('reviews/edit/<int:id>', ReviewsUpdateAPI.as_view()),
    path('reviews/update/<int:id>', ReviewsDeleteAPI.as_view())
]