from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView
from .forms import CompanyForm
from django.urls import reverse_lazy, reverse
from .models import Company
from django.conf import settings

# Create your views here.
class HomePageView(ListView):
    model = Company
    template_name = "home.html"


class CreateCompany(LoginRequiredMixin, CreateView):
    template_name = "company_form.html"
    form_class = CompanyForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class CompanyDetail(LoginRequiredMixin, DetailView):
    model = Company
    template_name = "detail_company.html"
    context_object_name = "company"


class CompanyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Company
    fields = ("name", "website", "phone", "logo", "country", "category")
    template_name = "company_edit.html"

    def test_func(self):
        user = self.request.user.username
        return user == "admin"

    def get_success_url(self):
        company = self.get_object()
        return reverse("company_detail", kwargs={"pk": company.pk})


class CompanyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Company
    template_name = "company_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        user = self.request.user.username
        return user == "admin"


class CompanyReviewDetailView(LoginRequiredMixin, DetailView):
    model = Company
    template_name = "review_company.html"
