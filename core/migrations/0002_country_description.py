# Generated by Django 5.0.7 on 2024-07-19 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="country",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
