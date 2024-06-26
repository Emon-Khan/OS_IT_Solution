# Generated by Django 4.2 on 2024-05-02 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osit', '0084_membership'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsroom',
            name='Job_Fair_Activity',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newsroom',
            name='MOU_SignIn_Activity',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newsroom',
            name='Nasa_App_Activity',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newsroom',
            name='Team_Activity',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newsroom',
            name='hiring_Activity',
            field=models.BooleanField(default=False),
        ),
    ]
