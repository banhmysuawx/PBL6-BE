from django.urls import path

from .views import FavoriteDetailView , FavoriteView ,ListJobFavoritesView,ListJobFavoritesView
urlpatterns = [
    path('favorites/list', ListJobFavoritesView.as_view()),
    path('favorites/create', FavoriteView.as_view()),
    path('favorites/detail/<int:pk>', FavoriteDetailView.as_view()),
    path('favorites/<int:user_id>', ListJobFavoritesView.as_view())
]
