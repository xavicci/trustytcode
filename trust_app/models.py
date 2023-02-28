from django.db import models
from django_countries.fields import CountryField
from django_project.settings import AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Nombre"
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Nombre"
    )
    website = models.URLField(null=False, blank=False, verbose_name="Sitio Web")
    phone = models.CharField(
        max_length=15, null=False, blank=False, verbose_name="Teléfono"
    )
    country = CountryField(verbose_name="País")
    logo = models.ImageField(upload_to="logos/")
    category = models.ManyToManyField(
        Category, related_name="get_categories", verbose_name="Categoría"
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    approved_company = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def approve(self):
        self.approved_company = True
        self.save()

    def __str__(self):
        return self.name


class Review(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="company_reviews"
    )
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(
        max_length=254, null=True, blank=True, verbose_name="Comentario"
    )
    RATING_CHOICES = [(i, "{} stars".format(i)) for i in range(1, 6)]
    rate = models.IntegerField(choices=RATING_CHOICES, default=5)
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación"
    )
    approved_review = models.BooleanField(default=False)

    def approve(self):
        self.approved_review = True
        self.save()

    def __str__(self):
        return self.text
