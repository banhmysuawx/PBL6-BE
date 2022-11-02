from django.urls import path

from .views import DisLikeCommentListAPI

urlpatterns = [
    path('dislikes', DisLikeCommentListAPI.as_view()),
    # path('companies/<int:pk>', CompanyDetailView.as_view()),
]
