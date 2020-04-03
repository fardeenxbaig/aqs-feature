# Generated by Django 3.0.3 on 2020-04-03 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(default=None, verbose_name='date of birth'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='mobile_no',
            field=models.CharField(default=None, max_length=20, verbose_name='mobile no'),
            preserve_default=False,
        ),
    ]