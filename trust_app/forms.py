from django import forms
from trust_app.models import Company, Category

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