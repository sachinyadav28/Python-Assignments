# Generated by Django 2.2.12 on 2020-05-07 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_management', '0004_auto_20200507_0651'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Authors', 'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name': 'Books and Authors', 'verbose_name_plural': 'Books'},
        ),
    ]
