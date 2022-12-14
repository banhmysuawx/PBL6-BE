"""joblink URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

# from accounts.views import *

schema_view = get_schema_view(
    openapi.Info(
        title="Jobs Link API",
        default_version="v1",
        description="Jobs Link Api Description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

def trigger_error(request):
    division_by_zero = 1 / 0
urlpatterns = [
    path(
        "",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("admin/", admin.site.urls),
    path("auth/", include("accounts.urls")),
    path('sentry-debug/', trigger_error),
    path("companies/" , include('companies.urls')),
    path("reviews/" , include('reviews.urls')),
    path("jobs/" , include('job.urls')),
    path("applicants/" , include('applicants.urls')),
    path("comment_posts/" , include('comment_posts.urls')),
    path("like_comments/" , include('like_comments.urls')),
    path("dislike_comments/" , include('dislike_comments.urls')),
    path("seekers/" , include('seekers.urls')),
    path("favorites/" , include('favorites.urls')),
    path("statisticals/" , include('statisticals.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.AVATAR_URL, document_root=settings.AVATAR_ROOT)