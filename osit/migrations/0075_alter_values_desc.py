# Generated by Django 4.2 on 2024-04-01 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osit', '0074_alter_service_feature_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='values',
            name='desc',
            field=models.TextField(max_length=300),
        ),
    ]
