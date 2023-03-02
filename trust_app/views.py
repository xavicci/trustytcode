from django.views.generic import DetailView, ListView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from .forms import CompanyForm, ReviewForm
from django.urls import reverse_lazy, reverse
from .models import Company, Category
from django.conf import settings
from django.db.models import Avg

# Create your views here.
class HomePageView(ListView):
    model = Company
    template_name = "home.html"

    def get_queryset(self):
        queryset = super().get_queryset().annotate(avg_rating=Avg('company_reviews__rate'))
        return queryset.filter(approved_company=True).order_by('-avg_rating')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
    



class CreateCompany(LoginRequiredMixin, CreateView):
    template_name = "company_form.html"
    form_class = CompanyForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class CompanyDetail(DetailView):
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


# class CompanyReviewDetailView(LoginRequiredMixin, DetailView):
#     model = Company
#     template_name = "review_company.html"
#     context_object_name = "company"


class CompanyReviewDetailView(View):
    def get(self, request, *args, **kwargs):
        view = ReviewGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ReviewPost.as_view()
        return view(request, *args, **kwargs)


class ReviewGet(DetailView):

    model = Company
    template_name = "review_company.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ReviewForm()
        return context


class ReviewPost(SingleObjectMixin, FormView):

    model = Company
    form_class = ReviewForm
    template_name = "review_company.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        review = form.save(commit=False)
        review.company = self.object
        review.save()
        return super().form_valid(form)

    def get_success_url(self):
        company = self.get_object()
        return reverse("review_company", kwargs={"pk": company.pk})
