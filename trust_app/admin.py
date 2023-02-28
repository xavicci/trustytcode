from django.contrib import admin

from .models import Company, Category, Review


class CommentInline(admin.TabularInline):
    model = Review
    extra = 0


class CompanyAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Company, CompanyAdmin)
admin.site.register(Category)
admin.site.register(Review)


# Register your models here.
