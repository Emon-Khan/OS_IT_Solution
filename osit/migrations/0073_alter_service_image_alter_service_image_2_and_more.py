# Generated by Django 4.2 on 2024-04-01 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osit', '0072_alter_service_image_alter_service_image_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='services/'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image_2',
            field=models.FileField(blank=True, null=True, upload_to='service/'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image_3',
            field=models.FileField(blank=True, null=True, upload_to='service/'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image_4',
            field=models.FileField(blank=True, null=True, upload_to='service/'),
        ),
    ]