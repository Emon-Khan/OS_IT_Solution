# Generated by Django 4.2 on 2024-04-01 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osit', '0076_alter_values_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsroom',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='NewsRoom/'),
        ),
        migrations.AlterField(
            model_name='newsroom',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='NewsRoom/'),
        ),
    ]