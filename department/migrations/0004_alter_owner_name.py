# Generated by Django 4.2.3 on 2023-07-20 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0012_alter_doctor_image'),
        ('department', '0003_owner_remove_department_gallery_ownergallery_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.category'),
        ),
    ]
