# Generated by Django 5.0.1 on 2024-01-18 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_rename_template_path_sitesection_url_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesection',
            name='url_path',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
