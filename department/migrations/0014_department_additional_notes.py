# Generated by Django 4.2.3 on 2023-07-20 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0013_alter_department_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='additional_notes',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
