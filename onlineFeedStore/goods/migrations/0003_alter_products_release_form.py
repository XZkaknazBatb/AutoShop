# Generated by Django 5.0 on 2024-05-31 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_products_image_small'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='release_form',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Форма выпуска'),
        ),
    ]
