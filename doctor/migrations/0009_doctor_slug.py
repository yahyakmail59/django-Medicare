# Generated by Django 4.2.3 on 2023-07-20 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0008_category_remove_doctor_department_doctor_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
