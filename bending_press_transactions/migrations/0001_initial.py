# Generated by Django 2.2.2 on 2019-08-31 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IronStoreTransaction',
            fields=[
                ('receipt_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('total_amount', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('notes', models.TextField()),
                ('cname', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('added_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='IronStoreTransactionItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('item_name', models.CharField(max_length=100)),
                ('item_quantity', models.IntegerField()),
                ('item_unit_price', models.IntegerField()),
                ('item_total_price', models.IntegerField(default=0)),
                ('added_at', models.DateTimeField()),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bending_press_transactions.IronStoreTransaction')),
            ],
        ),
        migrations.CreateModel(
            name='IronStoreTransactionHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.IntegerField()),
                ('damount', models.IntegerField(default=0)),
                ('added_at', models.DateTimeField()),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bending_press_transactions.IronStoreTransaction')),
            ],
        ),
    ]