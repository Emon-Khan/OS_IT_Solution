# Generated by Django 4.2 on 2024-03-24 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osit', '0040_website_setting_team_page_banner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='photo',
            field=models.ImageField(default=1, upload_to='team/'),
            preserve_default=False,
        ),
    ]
