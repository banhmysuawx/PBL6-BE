from django.urls import path

from companies.views import *

urlpatterns = [
    path('companies', CompanyListView.as_view()),
    path('companies/<int:pk>', CompanyDetailView.as_view()),
    path('companies/top_company', TopCompanyListView.as_view()),
    path('companies/sum_company', CountCompanyView.as_view()),
    path('companies-list/admin', CompanyListAdminView.as_view()),
    path('companies-detail/admin', CompanyDetailAdminView.as_view()),
    path('list-company', GetCompany.as_view()),
    path('company-profile/<int:user_id>', CompanyProfileView.as_view())
]
