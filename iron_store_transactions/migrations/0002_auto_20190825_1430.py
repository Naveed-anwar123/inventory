# Generated by Django 2.2.2 on 2019-08-25 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iron_store_transactions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ironstoretransaction',
            name='damount',
        ),
        migrations.RemoveField(
            model_name='ironstoretransaction',
            name='id',
        ),
        migrations.RemoveField(
            model_name='ironstoretransaction',
            name='item_id',
        ),
        migrations.RemoveField(
            model_name='ironstoretransaction',
            name='item_name',
        ),
        migrations.RemoveField(
            model_name='ironstoretransaction',
            name='item_quantity',
        ),
        migrations.RemoveField(
            model_name='ironstoretransaction',
            name='item_unit_price',
        ),
        migrations.RemoveField(
            model_name='ironstoretransaction',
            name='paid',
        ),
        migrations.AlterField(
            model_name='ironstoretransaction',
            name='discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ironstoretransaction',
            name='receipt_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='IronStoreTransactionItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('item_name', models.CharField(max_length=100)),
                ('item_quantity', models.IntegerField()),
                ('item_unit_price', models.IntegerField()),
                ('added_at', models.DateTimeField()),
                ('receipt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iron_store_transactions.IronStoreTransaction')),
            ],
        ),
        migrations.CreateModel(
            name='IronStoreTransactionHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.IntegerField()),
                ('damount', models.IntegerField(default=0)),
                ('item_unit_price', models.IntegerField()),
                ('added_at', models.DateTimeField()),
                ('receipt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iron_store_transactions.IronStoreTransaction')),
            ],
        ),
    ]
