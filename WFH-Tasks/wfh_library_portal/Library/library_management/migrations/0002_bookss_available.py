# Generated by Django 2.2.12 on 2020-05-06 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookss',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
