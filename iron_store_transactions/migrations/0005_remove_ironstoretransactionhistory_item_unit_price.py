# Generated by Django 2.2.2 on 2019-08-25 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iron_store_transactions', '0004_auto_20190825_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ironstoretransactionhistory',
            name='item_unit_price',
        ),
    ]