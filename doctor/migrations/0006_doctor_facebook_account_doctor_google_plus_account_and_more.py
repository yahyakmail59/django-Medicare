# Generated by Django 4.2.3 on 2023-07-19 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_alter_doctor_closing_time_mon_to_fri_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='facebook_account',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='google_plus_account',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='twitter_account',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='youtube_account',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
