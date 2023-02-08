from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("", include("trust_app.urls")),
    path("", include("allauth.urls")),
    path("accounts/", include("accounts.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
