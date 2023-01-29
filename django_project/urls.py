from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from django.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("trust_app.urls")),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]
