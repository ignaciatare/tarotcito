# Generated by Django 4.2.3 on 2023-07-24 11:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carta", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="carta",
            name="arcano",
            field=models.CharField(choices=[("MA", "Mayor"), ("ME", "Menor")], default="MA", max_length=5),
        ),
    ]
