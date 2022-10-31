from django.urls import path

from companies.views import CompanyListView , CompanyDetailView

urlpatterns = [
    path('companies', CompanyListView.as_view()),
    path('companies/<int:pk>', CompanyDetailView.as_view()),
]
