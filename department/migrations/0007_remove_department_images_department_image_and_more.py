# Generated by Django 4.2.3 on 2023-07-20 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0006_image_delete_gallery_remove_department_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='images',
        ),
        migrations.AddField(
            model_name='department',
            name='image',
            field=models.ImageField(default='', upload_to='department/'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]