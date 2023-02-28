from django import forms
from trust_app.models import Company, Category, Review
import requests


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = (
            "name",
            "website",
            "phone",
            "logo",
            "country",
            "category",
        )

    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("rate", "user", "text")
