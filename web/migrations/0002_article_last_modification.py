# Generated by Django 3.2.3 on 2022-01-08 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='last_modification',
            field=models.DateField(auto_now=True),
        ),
    ]