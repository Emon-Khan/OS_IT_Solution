# Generated by Django 4.2 on 2024-03-24 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osit', '0032_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='website_setting',
            old_name='career_page_banner',
            new_name='career_page_image',
        ),
        migrations.AddField(
            model_name='website_setting',
            name='career_form_image',
            field=models.ImageField(default=1, upload_to='img/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='website_setting',
            name='career_page_image_2',
            field=models.ImageField(default=1, upload_to='banner/'),
            preserve_default=False,
        ),
    ]
