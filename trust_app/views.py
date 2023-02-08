from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import CompanyForm
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

class CreateCompany(CreateView):
    template_name = "company_form.html"
    form_class = CompanyForm
    success_url = reverse_lazy("home")

