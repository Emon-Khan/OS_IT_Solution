# Generated by Django 4.2 on 2024-03-25 15:30

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osit', '0046_rename_professionals_of_company_website_setting_profession_of_company_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=30)),
                ('flag', models.FileField(upload_to='office/')),
                ('detail', ckeditor.fields.RichTextField(max_length=200)),
            ],
        ),
    ]
