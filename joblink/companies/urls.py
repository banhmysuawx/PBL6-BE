from django.urls import path

from companies.views import CompanyListView , CompanyDetailView,TopCompanyListView,CountCompanyView,CompanyDetailAdminView,CompanyListAdminView

urlpatterns = [
    path('companies', CompanyListView.as_view()),
    path('companies/<int:pk>', CompanyDetailView.as_view()),
    path('companies/top_company', TopCompanyListView.as_view()),
    path('companies/sum_company', CountCompanyView.as_view())
]
