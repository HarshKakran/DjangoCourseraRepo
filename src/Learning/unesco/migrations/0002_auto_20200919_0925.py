# Generated by Django 3.1 on 2020-09-19 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iso',
            old_name='value',
            new_name='name',
        ),
    ]