# Generated by Django 2.2.2 on 2019-09-07 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bending_press_transactions', '0003_auto_20190907_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ironstoretransaction',
            name='discount',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='ironstoretransaction',
            name='total_amount',
            field=models.CharField(max_length=100),
        ),
    ]
