from django.urls import path

from .views import CommentListView,AddCommentAPI,EditCommentAPI,DeleteCommentAPI

urlpatterns = [
    path('comments', CommentListView.as_view()),
    path('comments/create', AddCommentAPI.as_view()),
    path('comments/update/<int:pk>', EditCommentAPI.as_view()),
    path('comments/delete/<int:pk>', DeleteCommentAPI.as_view()),
]