# Generated by Django 3.2.13 on 2022-06-14 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0006_stocks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_by',
        ),
        migrations.AddField(
            model_name='product',
            name='created_by_id',
            field=models.PositiveIntegerField(default='1'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock_level',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.FloatField(),
        ),
    ]
