from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView
from .forms import CompanyForm
from django.urls import reverse_lazy
from .models import Company

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

class CreateCompany(CreateView):
    template_name = "company_form.html"
    form_class = CompanyForm
    success_url = reverse_lazy("home")

class CompanyDetail(DetailView):
    model = Company
    template_name = "detail_company.html"
    context_object_name = "company"




