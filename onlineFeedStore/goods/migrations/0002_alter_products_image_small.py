# Generated by Django 5.0 on 2024-05-31 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image_small',
            field=models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Изображение для каталога'),
        ),
    ]
