from rest_framework_simplejwt.views import TokenRefreshView

from django.urls import path
from django.views.generic import RedirectView
from .views import *

urlpatterns = [
    path("", RedirectView.as_view(url="login/", permanent=False)),
    path("register", RegisterView.as_view(), name="register"),
    path("email-verify", VerifyEmail.as_view(), name="email-verify"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("login", LoginView.as_view(), name="login"),
    path(
        "request-reset-email/",
        RequestPasswordResetEmail.as_view(),
        name="request-reset-email",
    ),
    path(
        "password-reset/<uidb64>/<token>/",
        PasswordTokenCheckAPI.as_view(),
        name="password-reset-confirm",
    ),
    path(
        "password-reset-complete",
        SetNewPasswordAPIView.as_view(),
        name="password-reset-complete",
    ),
    path("change-password", ChangePasswordView.as_view(), name="change-password"),
    path("me", GetMe.as_view(), name="me"),
    path("admin/list-accounts",GetAllAccounts.as_view()),
    path("admin/delete-accounts",DeleteUpdateAccount.as_view()),
    path("admin/sum-accounts",SumAccount.as_view()),
    path("admin/sum-seeker",SumSeeker.as_view()),
    path("admin/sum-employer",SumEmployer.as_view())
]
