# Generated by Django 4.2.3 on 2023-07-20 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0010_department_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='description',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]
