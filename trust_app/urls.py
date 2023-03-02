from django.urls import path
from .views import (
    HomePageView,
    CreateCompany,
    CompanyDetail,
    CompanyReviewDetailView,
    CompanyUpdateView,
    CompanyDeleteView,
    CompanyCategoryView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("review/<int:pk>", CompanyReviewDetailView.as_view(), name="review_company"),
    path("company/create", CreateCompany.as_view(), name="create_company"),
    path("company/<int:pk>", CompanyDetail.as_view(), name="company_detail"),
    path("company/<int:pk>/edit/", CompanyUpdateView.as_view(), name="company_edit"),
    path(
        "company/<int:pk>/delete/", CompanyDeleteView.as_view(), name="company_delete"
    ),
    path('category/<int:pk>/', CompanyCategoryView.as_view(), name='company_category'),
]
