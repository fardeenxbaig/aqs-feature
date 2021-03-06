# Generated by Django 3.0.3 on 2020-04-03 18:38

from django.db import migrations, models
import django.db.models.deletion
import fernet_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questionbank', '0002_auto_20200403_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='subquestion',
            name='question_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='questionbank.Question'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=fernet_fields.fields.EncryptedTextField(blank=True, null=True, verbose_name='question'),
        ),
    ]
