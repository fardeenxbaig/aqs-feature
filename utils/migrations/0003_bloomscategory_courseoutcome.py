# Generated by Django 3.0.3 on 2020-04-03 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0002_auto_20200403_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloomsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alt_text', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseOutcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('alt_text', models.CharField(max_length=10, unique=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.Courses')),
            ],
        ),
    ]
