# Generated by Django 4.2.3 on 2023-07-20 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0012_alter_department_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
