# Generated by Django 3.0 on 2020-08-06 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='draft',
            new_name='is_draft',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='publishing_date',
            new_name='published_date',
        ),
    ]