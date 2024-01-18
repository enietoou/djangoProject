# Generated by Django 5.0.1 on 2024-01-18 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_alter_statisticcontent_graph_image_path_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statisticcontent',
            name='graph_image_path',
            field=models.FileField(upload_to='mainapp/static/graph_images'),
        ),
        migrations.AlterField(
            model_name='statisticcontent',
            name='html_table_path',
            field=models.FileField(upload_to='mainapp/static/html_tables'),
        ),
    ]