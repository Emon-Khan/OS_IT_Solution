# Generated by Django 4.2 on 2024-03-23 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osit', '0019_delete_website_info_website_setting_about_of_company_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capabilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=100)),
                ('icon', models.FileField(upload_to='icon/')),
            ],
        ),
        migrations.RenameField(
            model_name='website_setting',
            old_name='capabilitis_section_banner',
            new_name='capabilities_section_banner',
        ),
        migrations.RenameField(
            model_name='website_setting',
            old_name='capabilitis_section_title',
            new_name='capabilities_section_title',
        ),
    ]
