# Generated by Django 5.0.1 on 2024-01-18 10:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0004_delete_currencyrate_delete_vacancy'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('template_path', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StatisticContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('html_table_path', models.CharField(max_length=255)),
                ('graph_image_path', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.sitesection')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.statisticcontent')),
            ],
        ),
    ]
