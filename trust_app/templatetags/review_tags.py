from django import template
from django.db.models import Avg
from ..models import Company

register = template.Library()

@register.filter
def average_review_rate(company):
    return company.company_reviews.aggregate(Avg('rate'))['rate__avg']
