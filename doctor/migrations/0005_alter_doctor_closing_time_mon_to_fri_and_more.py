# Generated by Django 4.2.3 on 2023-07-19 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_remove_doctor_closing_time_remove_doctor_day_of_week_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='closing_time_Mon_to_Fri',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='closing_time_Saturday',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='closing_time_Sunday',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='opening_time_Mon_to_Fri',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='opening_time_Saturday',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='opening_time_Sunday',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
