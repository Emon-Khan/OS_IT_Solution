# Generated by Django 4.2 on 2024-03-22 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osit', '0013_delete_client_partner_is_only_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social_Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=80)),
                ('icon', models.ImageField(upload_to='social_media')),
            ],
        ),
        migrations.RemoveField(
            model_name='website_info',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='website_info',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='website_info',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='website_info',
            name='twitter',
        ),
        migrations.RemoveField(
            model_name='website_info',
            name='youtube',
        ),
    ]
