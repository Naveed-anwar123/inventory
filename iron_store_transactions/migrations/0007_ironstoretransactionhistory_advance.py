# Generated by Django 2.2.2 on 2019-09-07 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iron_store_transactions', '0006_auto_20190907_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='ironstoretransactionhistory',
            name='advance',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
