# Generated by Django 3.2.7 on 2021-09-14 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EShop', '0004_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_items',
            name='quantity',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.FloatField(),
        ),
    ]
