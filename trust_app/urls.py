from django.urls import path
from .views import HomePageView, CreateCompany

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("company/create", CreateCompany.as_view(), name="create_company"),
]
