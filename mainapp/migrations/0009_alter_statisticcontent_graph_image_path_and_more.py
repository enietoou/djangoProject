# Generated by Django 5.0.1 on 2024-01-18 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_alter_sitesection_url_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statisticcontent',
            name='graph_image_path',
            field=models.FileField(upload_to='graph_images'),
        ),
        migrations.AlterField(
            model_name='statisticcontent',
            name='html_table_path',
            field=models.FileField(upload_to='html_tables'),
        ),
    ]
