# Generated by Django 4.2.3 on 2023-07-20 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0012_alter_doctor_image'),
        ('department', '0004_alter_owner_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='owner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='department.ownergallery'),
        ),
        migrations.AlterField(
            model_name='ownergallery',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.category'),
        ),
        migrations.DeleteModel(
            name='Owner',
        ),
    ]
