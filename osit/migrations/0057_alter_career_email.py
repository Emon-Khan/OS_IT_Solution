# Generated by Django 4.2 on 2024-03-26 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osit', '0056_website_setting_technology_icon_alter_career_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='email',
            field=models.EmailField(max_length=60, unique=True),
        ),
    ]