from django.urls import path
from .views import HomePageView, CreateCompany, CompanyDetail

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("company/create", CreateCompany.as_view(), name="create_company"),
    path("company/<int:pk>", CompanyDetail.as_view(), name="company_detail"),
]
