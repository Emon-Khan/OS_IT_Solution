# Generated by Django 4.2 on 2024-03-27 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osit', '0061_whychoseuspagesetting_values_section_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='website_setting',
            name='technology_page_banner',
            field=models.ImageField(default=1, upload_to='banner/'),
            preserve_default=False,
        ),
    ]
