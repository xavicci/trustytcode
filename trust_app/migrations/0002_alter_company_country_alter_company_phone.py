# Generated by Django 4.1.5 on 2023-02-08 01:11

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ("trust_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="country",
            field=django_countries.fields.CountryField(
                max_length=2, verbose_name="País"
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="phone",
            field=models.CharField(max_length=15, verbose_name="Teléfono"),
        ),
    ]
