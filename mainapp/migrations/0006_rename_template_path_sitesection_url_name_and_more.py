# Generated by Django 5.0.1 on 2024-01-18 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitesection',
            old_name='template_path',
            new_name='url_name',
        ),
        migrations.RemoveField(
            model_name='sitesection',
            name='url',
        ),
    ]
