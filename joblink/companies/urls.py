from django.urls import path

from . import views

urlpatterns = [
    path("companies", views.CompanyListView.as_view()),
    # path('companies/<int:id>', views.CompanyDetail.as_view()),
]
