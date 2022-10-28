from django.urls import path

from companies.views import CompanyListView , CompanyDetail ,CompanyCreateAPI ,CompanyUpdate,CompanyDelete

urlpatterns = [
    path('companies', CompanyListView.as_view()),
    path('companies/create', CompanyCreateAPI.as_view()),
    path('companies/<int:id>', CompanyDetail.as_view()),
    path('companies/delete/<int:id>', CompanyDelete.as_view()),
    path('companies/update/<int:id>', CompanyUpdate.as_view()),
]