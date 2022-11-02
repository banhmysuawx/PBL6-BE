from django.urls import path

from .views import LikeCommentListAPI

urlpatterns = [
    path('likes', LikeCommentListAPI.as_view()),
    # path('companies/<int:pk>', CompanyDetailView.as_view()),
]
