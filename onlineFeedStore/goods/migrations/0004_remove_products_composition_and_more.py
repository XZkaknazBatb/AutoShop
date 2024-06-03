# Generated by Django 5.0 on 2024-06-02 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_products_release_form'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='composition',
        ),
        migrations.RemoveField(
            model_name='products',
            name='feeding_standards',
        ),
        migrations.RemoveField(
            model_name='products',
            name='nutritional_info',
        ),
        migrations.RemoveField(
            model_name='products',
            name='recommendations',
        ),
        migrations.AlterField(
            model_name='products',
            name='release_form',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Объём'),
        ),
    ]
