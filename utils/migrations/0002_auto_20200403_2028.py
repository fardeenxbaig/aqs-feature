# Generated by Django 3.0.3 on 2020-04-03 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursecoordinators',
            name='course',
        ),
        migrations.AddField(
            model_name='coursecoordinators',
            name='course',
            field=models.ManyToManyField(to='utils.Courses'),
        ),
    ]
