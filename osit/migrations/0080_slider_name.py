# Generated by Django 4.2 on 2024-04-30 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osit', '0079_alter_slider_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
