# Generated by Django 4.2 on 2024-04-01 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osit', '0068_alter_service_feature_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='feature_title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
