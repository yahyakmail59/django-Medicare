# Generated by Django 4.2.3 on 2023-07-20 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0009_alter_departmentgallery_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
